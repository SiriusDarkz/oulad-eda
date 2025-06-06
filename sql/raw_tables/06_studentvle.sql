CREATE TABLE studentvle (
    id_student INT,
    id_site INT,
    code_module VARCHAR(45),
    code_presentation VARCHAR(45),
    date INT,
    sum_click INT,
    PRIMARY KEY (id_student, id_site),
    FOREIGN KEY (id_site)
        REFERENCES vle(id_site),
    FOREIGN KEY (id_student, code_module, code_presentation)
        REFERENCES studentinfo(id_student, code_module, code_presentation)
);