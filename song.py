# A python file to automatically write a post for Audr's Song Addiction
# in both English and Japanese.
# Run with `python3 song.py`

from datetime import datetime
from typing import Any
import requests

EN_POST_PATH: str = "_posts/"
JP_POST_PATH: str = "ja/_posts/"
EN_TEMPLATE_PATH: str = "_layouts/song-post/en.md"
JP_TEMPLATE_PATH: str = "_layouts/song-post/jp.md"
DATA_FILE_PATH: str = "_data/content/posts/song_addiction.yml"
POSTS_ASSETS_PATH: str = "assets/img/posts/"
OUTPUT_FILENAME_FORMAT: str = "{yyyy}-{mm}-{dd}-Song_{id}.md"


def main() -> None:
	count: int
	with open(DATA_FILE_PATH, "r", encoding="utf-8") as data_file:
		count = int(data_file.read().replace("count: ", ""))
	count += 1

	print("----- Song Addiction Post #%s -----" % count)
	youtube_url: str = input("YouTube URL: ")
	artist_name: str = input("Artist Name: ")
	en_title:    str = input("[EN] Title:  ")
	jp_title:    str = input("[JP] Title:  ")
	en_memo:     str = input("[EN] Memo:   ").strip()
	jp_memo:     str = input("[JP] Memo:   ").strip()

	en_title = en_title or jp_title
	jp_title = jp_title or en_title
	video_id: str = get_video_id(youtube_url)
	thumbnail_path: str = thumbnail_url(video_id)

	global now
	now = datetime.now()

	filename: str = get_filename(count)
	en_filename = EN_POST_PATH + filename
	jp_filename = JP_POST_PATH + filename
	write_post(
		EN_TEMPLATE_PATH, en_filename,
		count, thumbnail_path, video_id,
		artist_name, en_title, en_memo
	)
	write_post(
		JP_TEMPLATE_PATH, jp_filename,
		count, thumbnail_path, video_id,
		artist_name, jp_title, jp_memo
	)

	print("\nWritten new posts: ")
	print(en_filename)
	print(jp_filename)
	print("\nPost Song Addiction #%s" % count)

	# Increment count
	with open(DATA_FILE_PATH, "w", encoding="utf-8") as data_file:
		data_file.write("count: %s" % count)


def get_video_id(url: str) -> str:
    delete_list: list[str] = [
        "https://", "http://", "www.", "youtube.com/watch?v=",
        "youtu.be/", "youtube.com/embed/"
    ]

    # Clean the url using the delete_list
    video_id: str = url
    for string in delete_list:
        video_id = video_id.replace(string, "")

    # Trim the si identifier
    video_id = video_id.split("?si=")[0]

    return video_id


def get_filename(count: int) -> str:
    return OUTPUT_FILENAME_FORMAT.format(
        yyyy=now.strftime("%Y"),
        mm=now.strftime("%m"),
        dd=now.strftime("%d"),
        id=count
    )


def thumbnail_url(video_id: str) -> str:
	URL_FORMAT: str = "https://img.youtube.com/vi/%s/%s.jpg"
	SIZE_PRIORITY: list[str] = ["mqdefault", "hqdefault", "sddefault", "maxresdefault", "default"]

	selected_size: str
	for size in SIZE_PRIORITY:

		response = requests.get("https://img.youtube.com/vi/%s/%s.jpg" % (video_id, size))
		if response.ok:
			selected_size = size
			break

	return URL_FORMAT % (video_id, selected_size)


# def download_thumbnail(video_id: str) -> str:
# 	""" Downloads the thumbnail of the video and returns the file name in POSTS_ASSETS_PATH in this project """

# 	# sizes: list[str] = ["maxresdefault", "sddefault", "hqdefault", "mqdefault", "default"]
# 	sizes: list[str] = ["hqdefault", "mqdefault", "default", "maxresdefault", "sddefault"]

# 	thumbnail: bytes = b""
# 	for size in sizes:
# 		response = requests.get("https://img.youtube.com/vi/%s/%s.jpg" % (video_id, size))

# 		if response.ok:
# 			thumbnail = response.content
# 			break

# 	if thumbnail == b"":
# 		# Download failed somehow so use this as a default
# 		return "projects-heading-2024-10-23.jpg"

# 	filename: str = video_id + ".jpg"
# 	with open(POSTS_ASSETS_PATH + filename, "wb") as f:
# 		f.write(thumbnail)

# 	return filename


def write_post(
	template_path: str, output_path: str, id_number: int,
	thumbnail_path: str, video_id: str, artist_name: str,
	song_title: str, memo: str = ""
    ) -> None:

	date: str = now.strftime("%Y-%m-%d %H:%M:%S +0800")

	with open(template_path, "r", encoding="utf-8") as template_file:
		with open(output_path, "w", encoding="utf-8") as output_file:
			output_file.write(format(template_file.read(),
				id_number=id_number,
				thumbnail_filename=thumbnail_path,
				date=date,
				video_id=video_id,
				artist_name=artist_name,
				song_title=song_title,
				memo=memo
			))


def format(text: str, **keys: Any) -> str:
	formatted_text: str = text
	for key in keys:
		curled_key: str = "{%s}" % key
		value: str = str(keys[key])
		formatted_text = formatted_text.replace(curled_key, value)
	return formatted_text


if __name__ == "__main__":
    main()

