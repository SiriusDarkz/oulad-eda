CREATE TABLE students_infos (
    id_student INT,
    code_module VARCHAR(45),
    code_presentation VARCHAR(45),
    gender VARCHAR(3),
    region VARCHAR(45),
    highest_education VARCHAR(45),
    imd_band VARCHAR(16),
    age_band VARCHAR(16),
    num_of_prev_attempts INT,
    studied_credits INT,
    disability VARCHAR(3),
    final_result VARCHAR(45),
    PRIMARY KEY (id_student, code_module, code_presentation),
    FOREIGN KEY (code_module, code_presentation)
        REFERENCES courses(code_module, code_presentation)
);