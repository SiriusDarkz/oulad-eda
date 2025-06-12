CREATE TABLE IF NOT EXISTS courses_raw (
    code_module VARCHAR(45),
    code_presentation VARCHAR(45),
    module_presentation_length SMALLINT,
    PRIMARY KEY (code_module, code_presentation)
);