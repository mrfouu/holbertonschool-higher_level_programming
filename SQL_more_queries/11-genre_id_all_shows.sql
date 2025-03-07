-- This script lists all TV shows and their associated genre IDs from the database.
-- It displays: tv_shows.title - tv_show_genres.genre_id.
-- If a show doesn't have a genre, it will display NULL.
-- The results are sorted by tv_shows.title and tv_show_genres.genre_id.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
