-- This script lists all genres associated with the TV show 'Dexter'.
-- It displays: tv_genres.name.
-- The results are sorted by genre name in ascending order.
SELECT tv_genres.name FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
