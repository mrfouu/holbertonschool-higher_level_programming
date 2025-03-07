-- This script lists all TV shows that do not have a genre linked.
-- It displays: tv_shows.title - tv_show_genres.genre_id (which will be NULL for shows with no genre).
-- The results are sorted by tv_shows.title and tv_show_genres.genre_id.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
