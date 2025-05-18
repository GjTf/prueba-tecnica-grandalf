CREATE TABLE atenciones_medicas (
    patient_id VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    visit_date DATE,
    specialty VARCHAR(100),
    diagnosis TEXT,
    procedure TEXT,
    doctor_id VARCHAR(50),
    hospital_id VARCHAR(50),
    city VARCHAR(100),
    country VARCHAR(100),
    visit_type VARCHAR(50),
    visit_duration_minutes INT,
    outcome VARCHAR(50),
    readmission_within_30_days INT,
    cost_usd NUMERIC(10, 2)
);
