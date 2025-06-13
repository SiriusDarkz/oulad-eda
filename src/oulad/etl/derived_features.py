import pandas as pd

def calc_dropout_flags(df):
    df["was_dropped_out"] = df["date_unregistration"] < 999
    df["dropout_early"] = df["date_unregistration"] < 30
    return df

def calc_registration_timing(df):
    df["registered_late"] = df["date_registration"] > 20
    df["active_duration_days"] = df["date_unregistration"] - df["date_registration"]
    return df

def calc_vle_duration(df):
    df["duration_weeks"] = (df["week_to"] - df["week_from"]).clip(lower=0)
    return df

def calc_submission_flags(df, assessments_df):
    df = df.merge(
        assessments_df[["id_assessment", "date", "weight"]],
        on="id_assessment", how="left"
    )
    df["submitted"] = df["score"] >= 0
    df["on_time_submission"] = df["date_submitted"] <= df["date"]
    df["score_weighted"] = df["score"] * df["weight"] / 100
    return df.drop(columns=["date", "weight"])

def calc_vle_engagement(df, vle_df):
    df = df.merge(vle_df[["id_site", "activity_type", "week_from"]], on="id_site", how="left")
    df["early_engagement"] = df["date"] <= 20
    df["first_click_week"] = df.groupby("id_student")["week_from"].transform("min")
    df["total_clicks"] = df.groupby("id_student")["sum_click"].transform("sum")
    df["activity_diversity"] = df.groupby("id_student")["activity_type"].transform("nunique")
    df = df.drop(columns=["activity_type"])
    return df

# 🧩 Pipelines por entidad
def student_registration_pipeline(df):
    df = calc_dropout_flags(df)
    df = calc_registration_timing(df)
    return df

def vle_pipeline(df):
    return calc_vle_duration(df)

def student_assessment_pipeline(df, assessments_df):
    return calc_submission_flags(df, assessments_df)

def student_vle_pipeline(df, vle_df):
    return calc_vle_engagement(df, vle_df)

def apply_features(df: pd.DataFrame, table_name: str, **kwargs) -> pd.DataFrame:
    if table_name == "student_registrations":
        return student_registration_pipeline(df)
    elif table_name == "vles":
        return vle_pipeline(df)
    elif table_name == "student_assessments":
        return student_assessment_pipeline(df, kwargs["assessments_df"])
    elif table_name == "student_vles":
        return student_vle_pipeline(df, kwargs["vle_df"])
    else:
        return df