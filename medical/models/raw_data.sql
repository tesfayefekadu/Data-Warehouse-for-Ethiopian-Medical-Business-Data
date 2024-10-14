-- models/raw_data.sql
-- models/raw_data.sql

SELECT
    message_id,
    channel_title,
    channel_username,
    telegram_id,
    message,
    date,
    media_path
FROM {{ source'('public', 'medical_business_data')' }}
