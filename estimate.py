import math
import random
import unittest


def wallis(n):

    pi_appr = 1

    for i in range(1, n+1):
        pi_appr *= (4*i*i)/(4*i*i-1)

    pi_appr *= 2

    return pi_appr


def monte_carlo(n):
    '''
        circle => x^2 + y^2 - 1 = 0
        points inside the circle will be negative when plugged into the equation

        on the edge ? , assume that point belongs to the cirle

        square from (-1,0) to (1,0)

    '''

    ca = 0
    sa = 0

    for i in range(n):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1

        if (x*x + y*y - 1) <= 0:
            ca += 1
            sa += 1
        else:
            sa += 1

    return 4*ca/sa


class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15,
                            msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")

    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01,
                            msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)

        self.assertNotEqual(
            pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(
            pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4,
                            msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


if __name__ == "__main__":
    unittest.main()
