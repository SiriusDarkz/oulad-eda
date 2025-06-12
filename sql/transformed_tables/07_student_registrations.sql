CREATE TABLE IF NOT EXISTS student_registrations (
    id_student INTEGER NOT NULL,
    code_module CHAR(10) NOT NULL,
    code_presentation CHAR(10) NOT NULL,
    date_registration SMALLINT NOT NULL,
    date_unregistration SMALLINT NOT NULL,
    code_module_ordinal SMALLINT NOT NULL,
    code_presentation_ordinal SMALLINT NOT NULL,
    was_dropped_out BOOLEAN NOT NULL,
    dropout_early BOOLEAN NOT NULL,
    registered_late BOOLEAN NOT NULL,
    active_duration_days SMALLINT NOT NULL,
    PRIMARY KEY (id_student, code_module, code_presentation),
    FOREIGN KEY (id_student, code_module, code_presentation)
        REFERENCES student_infos(id_student, code_module, code_presentation)
);

CREATE INDEX IF NOT EXISTS idx_studentreg_student ON student_registrations(id_student);
CREATE INDEX IF NOT EXISTS idx_studentreg_module ON student_registrations(code_module);