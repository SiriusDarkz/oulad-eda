CREATE TABLE vles (
    id_site INT PRIMARY KEY,
    code_module VARCHAR(45),
    code_presentation VARCHAR(45),
    activity_type VARCHAR(45),
    week_from INT,
    week_to INT,
    FOREIGN KEY (code_module, code_presentation)
        REFERENCES courses(code_module, code_presentation)
);