-- This script lists all TV shows and their associated genres.
-- If a show doesn't have a genre, it will display NULL in the genre column.
-- The results are sorted by tv_shows.title and tv_genres.name in ascending order.

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
