import pygame


class Level():
    # def __init__(self,x1,x2,y1,y2):
    def __init__(self, ball, racket, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.center = (x2//2), (y2//2)
        self.p1_center = x1, y2//2
        self.p2_center = x2, y2//2
        self.player1 = racket(20, 100, self.p1_center[0], self.p1_center[1])
        self.player2 = racket(20, 100, self.p2_center[0]-20, self.p2_center[1])
        self.ball = ball(20, self.center[0], self.center[1])

        self.players = pygame.sprite.Group()
        self.all = pygame.sprite.Group()

        self.players.add(self.player1, self.player2)
        self.all.add(self.player1, self.player2, self.ball)

    def reset(self):
        pass

    def move_player(self, player):
        if player.moves == 1 and player.y + 100 <= self.y2:
            player.y += player.moves*5
        if player.moves == -1 and player.y > self.y1:
            player.y += player.moves*5

    def move_ball(self, speed):
        if self.ball.y == self.y1 or self.ball.y == self.y2:
            self.ball.speed_y = self.ball.speed_y*(-1)
            #self.ball.speed_x = self.ball.speed_x*(-1)
        if pygame.sprite.spritecollideany(self.ball, self.players) is None:
            self.ball.speed_y *= -1
            self.ball.speed_x *= -1
        self.ball.y += self.ball.speed_y
        self.ball.x += self.ball.speed_x

    def collision(self, object):
        if object.y < self.y2 and object.y > self.y1:
            return False
        return True
