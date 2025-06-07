CREATE TABLE students_registrations (
    id_student INT,
    code_module VARCHAR(45),
    code_presentation VARCHAR(45),
    date_registration INT,
    date_unregistration INT,
    PRIMARY KEY (id_student, code_module, code_presentation),
    FOREIGN KEY (id_student, code_module, code_presentation)
        REFERENCES students_infos(id_student, code_module, code_presentation)
);