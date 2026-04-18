CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_name) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE username = p_name;
    ELSE
        INSERT INTO phonebook(username, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE bulk_insert_contacts(names TEXT[], phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP

        IF phones[i] ~ '^[0-9+]+$' THEN
            INSERT INTO phonebook(username, phone)
            VALUES (names[i], phones[i]);
        END IF;

    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = p_value OR phone = p_value;
END;
$$;
