CREATE TABLE students_vles (
    id SERIAL PRIMARY KEY,
    code_module VARCHAR(45),
    code_presentation VARCHAR(45),
    id_student INT,
    id_site INT,
    date INT,
    sum_click INT,
    CONSTRAINT fk_student FOREIGN KEY (id_student)
        REFERENCES students_info(id_student),
    CONSTRAINT fk_vle FOREIGN KEY (id_site)
        REFERENCES vles(id_site)
);