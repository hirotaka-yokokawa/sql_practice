DROP TABLE IF EXISTS members;

CREATE TABLE members (
    name TEXT
);

--初期データの挿入
INSERT INTO members
    (name)
VALUES
    ('Bob'),
    ('Tom'),
    ('Ken')
;

