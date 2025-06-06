CREATE TABLE studentassessment (
    id_student INT,
    id_assessment INT,
    date_submitted INT,
    is_banked BOOLEAN,
    score FLOAT,
    PRIMARY KEY (id_student, id_assessment),
    FOREIGN KEY (id_assessment)
        REFERENCES assessments(id_assessment)
);