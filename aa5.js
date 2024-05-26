// 示例字符串，可能包含Unix/Linux风格的换行符(\n)或Windows风格的换行符(\r\n)
const originalString = `Willi Schroll
@wschroll
Reality is the canvas, mind the brush; perception paints our world.
G P T 4 S A I D
#mind
ALT
Quote
David S. Rosen, PhD
@DocDurDur
·
Mar 1
NEW RESEARCH: The Neuroscience of Creative Flow in Jazz Improvisation: An EEG Study

Delve into the secrets of creative flow in jazz improvisation and how experience affects these altered states of consciousness.

Read the full paper here: https://sciencedirect.com/science/article/pii/S0028393224000393…
Show more
6:00 AM · Mar 4, 2024
·
179
 Views
2
 Likes`;

// 使用正则表达式替换所有的换行符(\n或\r\n)为空格
const replacedString = originalString.replace(/(\r\n|\r|\n)/g, " ");

console.log(replacedString);
