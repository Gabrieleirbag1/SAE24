
CREATE TABLE mqtt_do (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mqid VARCHAR(100) NULL,
    date DATE NULL,
    heure VARCHAR(100) NULL,
    temp FLOAT NULL,
    mqnom VARCHAR(100) NULL
);

CREATE TABLE mqtt_mq (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idmqtt_id INT,
    nom VARCHAR(100) NOT NULL,
    piece VARCHAR(100) NOT NULL,
    emplacement VARCHAR(100) NOT NULL,
    mqdate DATE NULL,
    FOREIGN KEY (idmqtt_id) REFERENCES mqtt_do (id)
);


lancer le serveur

gunicorn -c conf/gunicorn_config.py SAE24.wsgi


