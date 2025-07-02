---
lng_pair: id_song_{id_number}
title: "Audr's Song Addiction #{id_number}"

category: song addiction
tags: [song, audrna]

img: "{thumbnail_filename}"

date: {date}

image_viewer_on: true
image_lazy_loader_on: true

memo: "{memo}"

---

<!-- outline-start -->
#### {song_title} / {artist_name}
<!-- outline-end -->

> On this day, Audr was vibing very hard to this song.

<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/{video_id}"
  title="YouTube video player"
  frameborder="0"
  allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
  data-align="center"
></iframe>

{% if page.memo != "" %}
<hr>

#### Audr's Memo

{{ page.memo }}
{% endif %}

