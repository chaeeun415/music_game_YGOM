import pygame
import time
import random
from graphics import *
import os
from pydub import AudioSegment
from pydub.playback import play
import simpleaudio

pygame.init()
display_width = 500
display_height = 500
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)

block_color = (53, 115, 255)

car_width = 73

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("game1")
clock = pygame.time.Clock()


def button(msg, x, y, width, height, inactive, active, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, inactive, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, active, (x, y, width, height))

    smallText = pygame.font.Font("BMJUA_ttf.ttf", 22)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(textSurf, textRect)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("BMJUA_ttf.ttf", 70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (200))
    screen.blit(TextSurf, TextRect)


def print_message(text, size, xpoint, ypoint):
    message = pygame.font.Font("BMJUA_ttf.ttf", size)
    TextSurf, TextRect = text_objects(text, message)
    TextRect.center = (xpoint, ypoint)
    screen.blit(TextSurf, TextRect)


def Falsemainrun():
    global mainrun
    mainrun = False
    global menurun
    menurun = True


def falsegame1run():
    global game1run
    game1run = False
    global menurun
    menurun = True


def falsegame2run():
    global game2run
    game2run = False
    global menurun
    menurun = True


def falsegame3run():
    global game3run
    game3run = False
    global menurun
    menurun = True


def gomenubutton():
    if game1run == True:
        button("Go Menu", 380, 20, 100, 40, (200, 0, 0), (230, 0, 0), falsegame1run)
    elif game2run == True:
        button("Go Menu", 380, 20, 100, 40, (200, 0, 0), (230, 0, 0), falsegame2run)
    elif game3run == True:
        button("Go Menu", 380, 20, 100, 40, (200, 0, 0), (230, 0, 0), falsegame3run)


def rungame1():
    global menurun
    menurun = False
    global game1run
    game1run = True


def rungame2():
    global menurun
    menurun = False
    global game2run
    game2run = True


def rungame3():
    global menurun
    menurun = False
    global game3run
    game3run = True


def nowupdate():
    screen.fill(pygame.color.Color(255, 255, 255))
    message_display("Now Update")
    gomenubutton()
    pygame.display.update()


def go_menu():
    screen.fill(pygame.color.Color(255, 255, 255))
    # showImage(80, 20, "C:/Users/박채은/Desktop/SW/music_game/background2-1.png")
    print_message("Y-GOM", 50, 250, 90)
    showImage(390, 10, "C:/Users/박채은/Desktop/SW/music_game/kids2.png")
    showImage(10, 390, "C:/Users/박채은/Desktop/SW/music_game/kids2.png")
    button("순간청력훈련", 140, 160, 220, 60, (255, 99, 71), (255, 127, 80), rungame1)
    button("동시청력훈련", 140, 250, 220, 60, (173, 255, 47), (124, 252, 000), rungame2)
    button("암기훈련", 140, 340, 220, 60, (135, 206, 250), (135, 206, 235), rungame3)
    pygame.display.update()


def go_main():
    screen.fill(pygame.color.Color(255, 255, 200))
    showImage(25, 70, "C:/Users/박채은/Desktop/SW/music_game/background1-1.png")
    message_display("Y-GOM")
    button("START!", 150, 270, 200, 50, (255, 182, 193), (255, 192, 203), Falsemainrun)
    # showImage(0, 0, "C:/Users/박채은/Desktop/SW/music_game/musicphoto5.jpg")
    pygame.display.update()

def selectlyrics():
    f = open("namedata.txt","r")
    songlist = []
    lyricslist = []
    printlyrics = []
    name = f.readline()
    while name:
        songlist.append(name)
        name = f.readline()
    for i in range(0,len(songlist)-1):
        newsonglist = songlist[i].replace("\n","")
        songlist[i] = newsonglist
    songnumber = random.randint(0, len(songlist)-1)
    answer = songlist[songnumber]
    filename = "C:/Users/박채은/Desktop/SW/music_game/lyrics/" + songlist[songnumber] + ".txt"
    f2= open(filename,"r")
    lyrics = f2.readline()
    while lyrics:
        lyricslist.append(lyrics)
        lyrics = f2.readline()
    for i in range(0,len(lyricslist)-1):
        newlyricslist = lyricslist[i].replace("\n","")
        lyricslist[i] = newlyricslist
    lyricsnumber = random.randint(0, len(lyricslist)-1)
    lyricsnumber2 = random.randint(0, len(lyricslist)-1)
    while lyricsnumber2 == lyricsnumber:
         lyricsnumber2 = random.randint(0, len(lyricslist)-1)
    return lyricslist[lyricsnumber], lyricslist[lyricsnumber2],answer


def showImage(x, y, path):
    image = pygame.image.load(path)
    screen.blit(image, (x, y))


def text_graphic_out1(x1, y1, x2, y2, fontSize, fontColour, ANSWER, msg_txt, txt_if_wrong):
    erase = Rectangle(Point(x1, y1), Point(x2, y2))
    erase.setFill(backgroundColor)
    erase.draw(win)
    if msg_txt == ANSWER:
        message = Text(erase.getCenter(), "정답입니다!")
        message.setFace('courier')
        message.setSize(fontSize)
        message.setTextColor(fontColour)
        message.draw(win)
    else:
        message = Text(erase.getCenter(), txt_if_wrong)
        message.setFace('courier')
        message.setSize(fontSize)
        message.setTextColor(fontColour)
        message.draw(win)
    return()


def text_graphic_out2(x1, y1, x2, y2, fontSize, fontColour, ANSWER, msg_txt, txt_if_wrong):
    erase = Rectangle(Point(x1, y1), Point(x2, y2))
    erase.setFill(color_rgb(255, 255, 200))
    erase.draw(win)
    if msg_txt in ANSWER:
        message = Text(erase.getCenter(), "정답입니다!")
        message.setFace('courier')
        message.setSize(fontSize)
        message.setTextColor(fontColour)
        message.draw(win)
    else:
        message = Text(erase.getCenter(), txt_if_wrong)
        message.setFace('courier')
        message.setSize(fontSize)
        message.setTextColor(fontColour)
        message.draw(win)
    return erase, message

def makeInputBox(x, y, fontSize, v_num, active):
    input_box = Entry(Point(x, y), v_num)
    # input_box = Entry(Point(center of the screen),
    # how many characters you can visibly see)
    input_box.setFill('yellow')    # color
    input_box.setFace('courier')     # font type
    input_box.setSize(fontSize)          # font size
    input_box.setStyle('italic')   # font style
    input_box.setTextColor('black')# text color
    input_box.draw(win)
    getMouse = active
    if getMouse:
        win.getMouse()                 # Wait for click in window
    text_in_input_box = input_box.getText()
    return input_box, (text_in_input_box)


def message(x, y, fontSize, msg_txt):
    txt = Text(Point(x, y), msg_txt)
    txt.setFace('courier')
    txt.setSize(fontSize)
    txt.draw(win)
    return txt

def countdown_message(x, y, fontSize, msg_txt, time1):
    txt = Text(Point(x, y), msg_txt)
    txt.setFace('courier')
    txt.setSize(fontSize)
    txt.draw(win)
    time.sleep(time1)
    txt.undraw()


def makeImage(x, y, imageFile):
    image = Image(Point(x, y), imageFile)
    image.draw(win)
    return image



def getMusic(path):
    musicTitle_lst = os.listdir(path)
    temp_list = (random.choice(musicTitle_lst)).split(".")
    musicTitle = temp_list[0]
    return musicTitle

def musicPlay(musicName):
    music = pygame.mixer.music.load('C:/Users/박채은/Desktop/SW/music_game/music/{}.mp3'.format(musicName))
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.mixer.music.set_volume(1.0)  # 볼륨설정
    pygame.mixer.music.set_pos(60)  # 노래를 시작하는 시간을 설정(노래 60초부터 재생하라는 의미)
    pygame.mixer.music.fadeout(2000)  # 특정 시간동안 노래 재생한 후 fadeout/millisecond 기준이라 1000설정하면 1초 동안 재생됨.


def inform_score(correct_number, stage_number):
    inform_score_box = Rectangle(Point(490, 490), Point(10, 10))
    inform_score_box.setFill(color_rgb(255, 228, 255))
    inform_score_box.draw(win)
    background_image12 = Image(Point(250, 115), "bubble2.png")
    background_image12.draw(win)
    score_message = Text(Point(250, 100), "당신의 점수는\n {} / {} 입니다".format(correct_number, stage_number))
    score_message.setFace('courier')
    score_message.setSize(35)
    score_message.setTextColor('black')
    score_message.draw(win)

def musicSegment(time):
    song_for_mixed1 = getMusic('C:/Users/박채은/Desktop/SW/music_game/music')
    song_for_mixed2 = getMusic('C:/Users/박채은/Desktop/SW/music_game/music')
    song_for_mixed3 = getMusic('C:/Users/박채은/Desktop/SW/music_game/music')
    while song_for_mixed1 == song_for_mixed2:
        song_for_mixed2 = getMusic('C:/Users/박채은/Desktop/SW/music_game/music')
    while song_for_mixed3 == song_for_mixed1 or song_for_mixed3 == song_for_mixed2:
        song_for_mixed3 = getMusic('C:/Users/박채은/Desktop/SW/music_game/music')
    audio1 = AudioSegment.from_file("C:/Users/박채은/Desktop/SW/music_game/music/{}.mp3".format(song_for_mixed1))
    audio2 = AudioSegment.from_file("C:/Users/박채은/Desktop/SW/music_game/music/{}.mp3".format(song_for_mixed2))
    audio3 = AudioSegment.from_file("C:/Users/박채은/Desktop/SW/music_game/music/{}.mp3".format(song_for_mixed3))

    mixed2 = audio1.overlay(audio2)                               #combine , superimpose audio files
    mixed3 = mixed2.overlay(audio3)
    # mixed3.export("mixed.mp3", format = "wav")
    mixed3 = mixed3[60000 : 60000 + time]
    play(mixed3)
    return song_for_mixed1, song_for_mixed2, song_for_mixed3


mainrun = True
run = True
menurun = False
game1run = False
game2run = False
game3run = False
datatuple, masktuple = pygame.cursors.compile(pygame.cursors.thickarrow_strings, black='X', white='.', xor='o')
pygame.mouse.set_cursor(*pygame.cursors.arrow)

while run:
    while mainrun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainrun = False
                pygame.quit()
                quit()

            clock.tick(60)
            go_main()

    while menurun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menurun = False
                pygame.quit()
                quit()

            clock.tick(60)
            go_menu()

    while game1run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game1run = False
                pygame.quit()
                quit()

            clock.tick(60)

            chance = 0
            stage_number1 = 5
            correct_number1 = 0
            played_before_1 = []
            while chance < stage_number1:
                win_x = 500
                win_y = 500
                backgroundColor = color_rgb(255, 255, 200)
                win = GraphWin("Input Text", win_x, win_y)
                win.setBackground('white')

                music_name = getMusic('C:/Users/박채은/Desktop/SW/music_game/music')
                while music_name in played_before_1:
                    music_name = getMusic('C:/Users/박채은/Desktop/SW/music_game/music')
                ANSWER = music_name.upper()
                played_before_1.append(music_name)

                countdown_message(250, 250, 35, "stage{}".format(chance + 1), 1)
                # countdown_message(250, 250, 35, "3", 1)
                # countdown_message(250, 250, 35, "2", 1)
                # countdown_message(250, 250, 35, "1", 1)
                # countdown_message(250, 250, 35, "GO!", 1)

                count_image13 = makeImage(250, 250, '3image.png')
                time.sleep(1)
                count_image12 = makeImage(250, 250, '2image.png')
                time.sleep(1)
                count_image11 = makeImage(250, 250, '1image.png')
                time.sleep(1)
                go_image1 = makeImage(250, 250, 'goimage.png')
                time.sleep(0.5)
                count_image13.undraw()
                count_image12.undraw()
                count_image11.undraw()
                go_image1.undraw()


                musicPlay(music_name)
                time.sleep(4)

                message(250, 160, 30, "노래 제목을 입력하세요")
                enter_image1 = makeImage(250, 80, '@people.png')
                for x in range(0, 1, 1):
                    input_box1, my_answer = makeInputBox(250, 215, 30, 10, True)
                    my_answer = my_answer.upper()
                    text_graphic_out1(450, 400, 50, 300, 15, 'red', ANSWER, my_answer, "다시 도전하세요!")
                    if my_answer != ANSWER:
                        input_box2, my_answer2 = makeInputBox(250, 215, 30, 10, True)
                        my_answer2 = my_answer2.upper()
                        text_graphic_out1(450, 400, 50, 300, 15, 'red', ANSWER, my_answer2, "마지막 기회입니다")
                        if my_answer2 != ANSWER:
                            input_box3, my_answer3 = makeInputBox(250, 215, 30, 10, True)
                            my_answer3 = my_answer3.upper()
                            text_graphic_out1(450, 400, 50, 300, 15, 'red', ANSWER, my_answer3, "정답은\n\"{}\"\n입니다.".format(music_name))
                            if chance <= stage_number1 - 2:
                                message(340, 440, 15, "화면을 클릭하면 다음 단계로!")
                            else:
                                countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                                time.sleep(1)
                                countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                                input_box3.undraw()
                                input_box2.undraw()
                                input_box1.undraw()
                            if my_answer3 == ANSWER:
                                correct_number1 += 1
                        else:
                            if chance <= stage_number1 - 2:
                                message(340, 440, 15, "화면을 클릭하면 다음 단계로!")
                            else:
                                countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                                time.sleep(1)
                                countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                                input_box2.undraw()
                                input_box1.undraw()
                            correct_number1 += 1

                    else:
                        if chance <= stage_number1 - 2:
                            message(340, 440, 15, "화면을 클릭하면 다음 단계로!")
                        else:
                            countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                            time.sleep(1)
                            countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                            input_box1.undraw()
                        correct_number1 += 1
                    if chance == stage_number1 - 1:
                        inform_score(correct_number1, stage_number1)
                        image2 = Image(Point(250, 330), "happyperson.png")
                        image2.draw(win)

                win.getMouse()
                time.sleep(1)
                win.close()
                chance += 1
                print(chance)

            game1run = False
            pygame.quit()
            quit()


    while game2run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game2run = False
                pygame.quit()
                quit()

            clock.tick(60)
            for x in range(0, 1, 1):
                win_x = 500
                win_y = 500
                backgroundColor = color_rgb(255, 255, 255)
                win = GraphWin("MusicSegment", win_x, win_y)
                win.setBackground(backgroundColor)

                # countdown_message(250, 250, 35, "3", 1)
                # countdown_message(250, 250, 35, "2", 1)
                # countdown_message(250, 250, 35, "1", 1)
                # countdown_message(250, 250, 35, "GO!", 1)
                count_image23 = makeImage(250, 250, '3image.png')
                time.sleep(1)
                count_image22 = makeImage(250, 250, '2image.png')
                time.sleep(1)
                count_image21 = makeImage(250, 250, '1image.png')
                time.sleep(1)
                go_image2 = makeImage(250, 250, 'goimage.png')
                count_image23.undraw()
                count_image22.undraw()
                count_image21.undraw()
                go_image2.undraw()


                # 노래 나오게
                loading_txt = message(250, 100, 30, "노래가\n재생되는\n중입니다")
                loading_image = makeImage(250, 300, 'loading3.png')
                ANSWER_mixed1, ANSWER_mixed2, ANSWER_mixed3 = musicSegment(20000)
                loading_txt.undraw()
                loading_image.undraw()

                ANSWER_for_mixed = [ANSWER_mixed1.upper(), ANSWER_mixed2.upper(), ANSWER_mixed3.upper()]
                # 입력하면 답과 비교해서 몇 개 맞았는지 알려주는 결과창 만들기

                # 입력받기
                correct_number2 = 0
                music_number2 = 3
                input_message2 = message(250, 100, 20, "노래 제목을 입력하세요\n노래 입력 순서는 상관이 없습니다\n노래 한 곡 당 입력 기회는 한 번입니다")

                input_box21, answer21 = makeInputBox(250, 215, 30, 10, True)
                answer21 = answer21.upper()
                box21, message21 = text_graphic_out2(400, 380, 100, 280, 20, 'black', ANSWER_for_mixed, answer21, '정답이 아닙니다')
                inform21 = message(340, 440, 14, "화면을 클릭하면 다음 노래 입력 가능!")
                if answer21 in ANSWER_for_mixed:
                    correct_number2 += 1
                win.getMouse()
                inform21.undraw()
                input_box21.undraw()
                box21.undraw()
                message21.undraw()

                input_box22, answer22 = makeInputBox(250, 215, 30, 10, True)
                answer22 = answer22.upper()
                box22, message22 = text_graphic_out2(400, 380, 100, 280, 20, 'black', ANSWER_for_mixed, answer22, '정답이 아닙니다')
                inform22 = message(340, 440, 14, "화면을 클릭하면 다음 노래 입력 가능!")
                if answer22 in ANSWER_for_mixed:
                    correct_number2 += 1
                win.getMouse()
                inform22.undraw()
                input_box22.undraw()
                box22.undraw()
                message22.undraw()

                input_box23, answer23 = makeInputBox(250, 215, 30, 10, True)
                answer23 = answer23.upper()
                box23, message23 = text_graphic_out2(400, 380, 100, 280, 20, 'black', ANSWER_for_mixed, answer23, '정답이 아닙니다')
                inform23 = message(340, 440, 14, "화면을 클릭하면 결과 창으로!")
                if answer23 in ANSWER_for_mixed:
                    correct_number2 += 1
                win.getMouse()
                inform23.undraw()
                input_box23.undraw()
                box23.undraw()
                message23.undraw()
                input_message2.undraw()

                time.sleep(1)

                inform_music_box = Rectangle(Point(490, 490), Point(10, 10))
                inform_music_box.setFill(color_rgb(255, 240, 255))
                inform_music_box.draw(win)
                makeImage(250, 250, 'background1-3.png')
                message(250, 225, 17, "정답\n1. {}\n2. {}\n3. {}".format(ANSWER_mixed1, ANSWER_mixed2, ANSWER_mixed3))
                win.getMouse()
                inform_score(correct_number2, music_number2)
                image2 = Image(Point(250, 330), "happyperson.png")
                image2.draw(win)
                win.getMouse()
                win.close()
                game2run = False
                pygame.quit()
                quit()

    while game3run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game3run = False
                pygame.quit()
                quit()

            clock.tick(60)
            chance = 0
            stage_number3 = 5
            correct_number3 = 0
            played_before_3 = []
            while chance < stage_number3:
                win_x = 500
                win_y = 500
                backgroundColor = color_rgb(255, 255, 200)
                win = GraphWin("Input Text", win_x, win_y)
                win.setBackground('white')

                countdown_message(250, 250, 35, "stage{}".format(chance + 1), 1)
                # countdown_message(250, 250, 35, "3", 1)
                # countdown_message(250, 250, 35, "2", 1)
                # countdown_message(250, 250, 35, "1", 1)
                # countdown_message(250, 250, 35, "GO!", 1)
                count_image33 = makeImage(250, 250, '3image.png')
                time.sleep(1)
                count_image32 = makeImage(250, 250, '2image.png')
                time.sleep(1)
                count_image31 = makeImage(250, 250, '1image.png')
                time.sleep(1)
                go_image3 = makeImage(250, 250, 'goimage.png')
                time.sleep(1)
                count_image33.undraw()
                count_image32.undraw()
                count_image31.undraw()
                go_image3.undraw()

                l1, l2, ANSWER = selectlyrics()
                if ANSWER in played_before_3:
                    l1, l2, ANSWER = selectlyrics()
                played_before_3.append(ANSWER)
                ANSWER1 = ANSWER.upper()
                message(250, 50, 15, l1)
                message(250, 100, 15, l2)

                message(250, 170, 30, "노래 제목을 입력하세요")
                # enter_image3 = makeImage(250, 80, '@people.png')
                for x in range(0, 1, 1):
                    input_box1, my_answer = makeInputBox(250, 225, 30, 10, True)
                    my_answer = my_answer.upper()
                    text_graphic_out1(450, 400, 50, 300, 15, 'red', ANSWER1, my_answer, "다시 도전하세요!")
                    if my_answer != ANSWER1:
                        input_box2, my_answer2 = makeInputBox(250, 225, 30, 10, True)
                        my_answer2 = my_answer2.upper()
                        text_graphic_out1(450, 400, 50, 300, 15, 'red', ANSWER1, my_answer2, "마지막 기회입니다")
                        if my_answer2 != ANSWER1:
                            input_box3, my_answer3 = makeInputBox(250, 225, 30, 10, True)
                            my_answer3 = my_answer3.upper()
                            text_graphic_out1(450, 400, 50, 300, 15, 'red', ANSWER1, my_answer3, "정답은\n\"{}\"\n입니다.".format(ANSWER))
                            if chance <= stage_number3 - 2:
                                message(340, 440, 15, "화면을 클릭하면 다음 단계로!")
                            else:
                                countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                                time.sleep(1)
                                countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                                input_box3.undraw()
                                input_box2.undraw()
                                input_box1.undraw()
                            if my_answer3 == ANSWER1:
                                correct_number3 += 1
                        else:
                            if chance <= stage_number3 - 2:
                                message(340, 440, 15, "화면을 클릭하면 다음 단계로!")
                            else:
                                countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                                time.sleep(1)
                                countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                                input_box2.undraw()
                                input_box1.undraw()
                            correct_number3 += 1

                    else:
                        if chance <= stage_number3 - 2:
                            message(340, 440, 15, "화면을 클릭하면 다음 단계로!")
                        else:
                            countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                            time.sleep(1)
                            countdown_message(330, 440, 15, "게임이 끝났습니다", 1)
                            input_box1.undraw()
                        correct_number3 += 1
                    if chance == stage_number3 - 1:
                        inform_score(correct_number3, stage_number3)
                        image2 = Image(Point(250, 330), "happyperson.png")
                        image2.draw(win)

                win.getMouse()
                time.sleep(1)
                win.close()
                chance += 1
                print(chance)

            game3run = False
            pygame.quit()
            quit()


pygame.quit()