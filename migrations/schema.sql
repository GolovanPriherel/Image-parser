BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> a541b3f98f47

CREATE TABLE rule34_images_info (
    image_url VARCHAR, 
    image_id VARCHAR[], 
    image_copyrights VARCHAR[], 
    image_character_tag VARCHAR[], 
    image_artists VARCHAR[], 
    image_tags VARCHAR[], 
    image_metadata VARCHAR[], 
    image_path VARCHAR[], 
    image_website VARCHAR, 
    image_rating INTEGER, 
    published_at VARCHAR, 
    parsed BOOLEAN, 
    inserted_at TIMESTAMP WITHOUT TIME ZONE
);

ALTER TABLE rule34_image_info ADD CONSTRAINT pk_image_url PRIMARY KEY (image_url);

INSERT INTO alembic_version (version_num) VALUES ('a541b3f98f47') RETURNING alembic_version.version_num;

COMMIT;

