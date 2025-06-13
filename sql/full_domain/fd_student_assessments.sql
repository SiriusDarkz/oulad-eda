CREATE OR REPLACE VIEW fd_student_assessments AS
SELECT
    -- Clave única por estudiante y evaluación
    sa.id_student,
    sa.id_assessment,
    a.assessment_type,

    -- Datos del curso
    c.code_module,
    c.code_presentation,
    si.region,
    si.gender,
    si.highest_education,
    si.imd_band,
    si.age_band,
    si.num_of_prev_attempts,
    si.studied_credits,
    si.disability,
    si.final_result,
    si.date_registration,
    si.date_unregistration,

    -- Datos de la evaluación
    sa.date_submitted,
    sa.score,
    sa.score_weighted,
    sa.submitted,
    sa.on_time_submission,
    sa.is_banked,

    -- Actividad en el entorno VLE (sumarizada por tipo)
    sv.n_days_dataplus,
    sv.n_days_dualpane,
    sv.n_days_externalquiz,
    sv.n_days_folder,
    sv.n_days_forumng,
    sv.n_days_glossary,
    sv.n_days_homepage,
    sv.n_days_htmllactivity,
    sv.n_days_oucollaborate,
    sv.n_days_oucontent,
    sv.n_days_oureference,
    sv.n_days_resource,
    sv.n_days_sharedsubpage,
    sv.n_days_subpage,
    sv.n_days_url,
    sv.n_days_page,
    sv.total_clicks,
    sv.activity_diversity,
    sv.early_engagement,

    -- Ordinales
    si.gender_ordinal,
    si.region_ordinal,
    si.highest_education_ordinal,
    si.imd_band_ordinal,
    si.age_band_ordinal,
    si.disability_ordinal,
    si.final_result_ordinal,
    c.code_module_ordinal,
    c.code_presentation_ordinal,
    a.assessment_type_ordinal,
    sa.is_banked_ordinal

FROM student_assessments sa
JOIN assessments a ON sa.id_assessment = a.id_assessment
JOIN student_infos si ON sa.id_student = si.id_student
                      AND a.code_module = si.code_module
                      AND a.code_presentation = si.code_presentation
JOIN courses c ON a.code_module = c.code_module AND a.code_presentation = c.code_presentation
LEFT JOIN student_vles sv ON sa.id_student = sv.id_student
                          AND a.code_module = sv.code_module
                          AND a.code_presentation = sv.code_presentation;