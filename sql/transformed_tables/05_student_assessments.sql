CREATE TABLE IF NOT EXISTS student_assessments (
    id_assessment INTEGER NOT NULL,
    id_student INTEGER NOT NULL,
    date_submitted SMALLINT NOT NULL,
    is_banked BOOLEAN NOT NULL,
    score FLOAT NOT NULL,
    is_banked_ordinal SMALLINT NOT NULL,
    submitted BOOLEAN NOT NULL,
    on_time_submission BOOLEAN NOT NULL,
    score_weighted FLOAT NOT NULL,
    PRIMARY KEY (id_assessment, id_student),
    FOREIGN KEY (id_assessment) REFERENCES assessments(id_assessment)
);

CREATE INDEX IF NOT EXISTS idx_studentassessment_student ON student_assessments(id_student);
