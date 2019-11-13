# Theseus-Minotaus-Labyrinth

Те, кто получили классическое образование, могут помнить легенду о Тезее и Минотавре. Это миф о быкоголовом монстре, клубках шелка и подземных лабиринтпх, полных однообразных запутанных пещер. Теперь мы узнаем, что же произошло на самом деле.

Лабириет состоял из нескольких пещер, соединенных проходами. Тезею удалось незаметно пронести в лабиринт запас свеч и небольшой тюбик фосфоресцирующей краски, которой он мог отмечать свой путь, вернее, проходы, в которых он побывал. Тезей знал, что он заключен в лабиринте и что он сможет выбраться, если найдет и убьет Минотавра. Он выбрал следующую стратегию: двигаться осторожно вдоль прохода до тех пор, пока не достигнет пещеры, затем повернуть направо (он был левшой и хотел держать меч подальше от стены) и двигаться вдоль стены до выхода из пещеры. Если выход не был помечен, то Тезей пометит его и будет двигаться по этому проходу. Если он услышит Минотавра в одной с ним пещере, то он зажжет свечу и убьет ослепленного светом Минотавра. Однако, если Тезей входит в пещеру, уже помеченную Минотавром, он зажжет свечу и оставит ее в этой пещере, а затем повернет направо, как обычно, но пойдет за Минотавром.

В то же время, Минотавр тоже ищет Тезея. Он был большего размера и двигался медленнее, но хорошо знал пещеры и проходы и тоже петешествовал по лабиринту, как и Тезей, но выбирал другие проходы. Минотавр поворачивал налево, когда попадал в ещё не помеченную им пещеру, и двигался по ней по часовой стрелке, пока не находил не помеченного им выхода, который он помечал и затем двигался по нему. Если он чувствовал, что в пещере, куда он собирался войти, горит свеча, то он поворачивал обратно, возвращаясь в пещеру и тем самым заканчивая свой "ход".

Рассмотрим следующий лабиринт:
![alt text](https://i.ibb.co/sjww3Mt/labirint-Tes.png)

Предположим, что Тезей начинает между А и С, направляясь к С, а Минотавр стартует между F и H, двигаясь к H. После того, как Тезей достигает С, он пойдет в направлении D, тогда как Минотавр, попав в H, направится к G. Затем Тезй пойдет к G, пока Минотавр будет направляться к D, и Тезей будет убит в коридоре между D и G. Однако, если Тезей будет начинать таж же, а Минотавр стартует между D и G, пока Тезей движется из С через D к G, Минотавр пройдет из G через E к F. Когда Тезей достигнет G, он обнаружит, что Минотавр уже был здесь до него и направлялся к E, а не к H. Двигаясь за Минотавром, Тезей достигает Е в тот момент, когда Минотавр приходит в H. Минотавр пытается пройти в G, но, испугавшисб поставленной там Тезеем свечи, возвращается в H. Тезей тем временет приходит в F, идя по следам Минотавра. Пока Минотавр безуспешно пытается пройти в E, но испугавшись свечи, возвращается обратно, Тезей достигает H, где и убивает Минотавра, ослепив его.

Напишите программу, имитирующую поединок Тезея и Минотавра.

# Входные данные.
Входные данные представляют собой набор лабиринтов. Каждый лабиринт состоит из нескольких пещер, каждая из которых описана в отдельной строке.  
Каждая строка файла входных данных содержит идентификатор пещеры, латинскую прописную букву, за которой следует двоеточие (:) и список проходов, соединяющих эту пещеру с другими, причем список упорядочен так, что проходы описываются в порядке против часовой стрелки. Ни одна пещера не соединяется с собой. Описания пещер не упорядочены. Символ @ обозначает конец описания очередного лабиринта, следующие за ним две пары символов обозначают стартовое положение Тезея и Минотавра. Первая пара обозначает проход, с которого начинает Тезей, вторая - Минотавр. Направление движения задается вторым символом пары. Конец файла обозначается символом #.  
Для каждого набора данных предусмотрено решение за конечное число шагов, т.е. ничьи быть не может.

# Пример входных данных
A:BCD  
D:BACG  
F:HE  
G:HED  
B:AD  
E:FGH  
H:FEG  
C:AD  
@ACFH  
A:BCD  
D:BACG  
F:HE  
G:HED  
B:AD  
E:FGH  
H:FEG  
C:AD  
@ACDG  
\#  

# Выходные данные.
В файле с выводом программы каждая строка соответствует одному лабиринту из входных данных. В каждой строке должно быть указано, кто же в итоге был убит и где, причем с точки зрения Тезея, то есть если встреча, произошла в проходе, к несчастью для Тезея, то необходимо указать две пещеры, которые соединяются этим проходом, иначе - одну пещеру, где был убит Минотавр.

# Пример выходных данных
Theseus is killed between D and G  
The Minotaur is slain in H
