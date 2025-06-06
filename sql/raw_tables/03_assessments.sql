CREATE TABLE assessments (
    id_assessment INT PRIMARY KEY,
    code_module VARCHAR(45),
    code_presentation VARCHAR(45),
    assessment_type VARCHAR(45),
    date INT,
    weight SMALLINT,
    FOREIGN KEY (code_module, code_presentation)
        REFERENCES courses(code_module, code_presentation)
);