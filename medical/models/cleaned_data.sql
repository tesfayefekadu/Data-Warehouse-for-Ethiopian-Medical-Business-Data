-- models/cleaned_data.sql

WITH cleaned AS (
    SELECT
        message_id,
        channel_title,
        channel_username,
        telegram_id,
        message,
        date,
        media_path
    FROM {{ ref('raw_data') }}  -- Reference the raw data model
    WHERE date IS NOT NULL  -- Remove rows with missing dates
    AND message IS NOT NULL -- Remove rows with missing messages
    AND message_id IS NOT NULL  -- Ensure telegram_id is valid
    GROUP BY 
        message_id, 
        channel_title, 
        channel_username, 
        telegram_id, 
        message, 
        date, 
        media_path
)

SELECT * FROM cleaned
