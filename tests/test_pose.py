from math import pi, sqrt, isclose

from gym_navigation.utils.pose import Pose, Point


class TestLine:
    def test_pose_equality(self):
        pose1 = Pose(Point(1, 2), pi / 4)
        pose2 = Pose(Point(1, 2), pi / 4)
        assert pose1 == pose2

    def test_pose_inequality(self):
        pose1 = Pose(Point(1, 2), pi / 4)
        pose2 = Pose(Point(1, 2), pi / 3)
        assert pose1 != pose2

    def test_valid_yaw_greater_than_pi(self):
        pose = Pose(Point(1, 2), 3 * pi / 2)
        assert pose.yaw == -pi / 2

    def test_valid_yaw_less_than_negative_pi(self):
        pose = Pose(Point(1, 2), -3 * pi / 2)
        assert pose.yaw == pi / 2

    def test_move_with_yaw_zero(self):
        pose = Pose(Point(1, 2), 0)
        pose.move(1)
        expected_pose = Pose(Point(1, 3), 0)
        assert expected_pose == pose

    def test_move_with_yaw_pi(self):
        pose = Pose(Point(1, 2), pi)
        pose.move(1)
        expected_pose = Pose(Point(1, 1), pi)
        assert expected_pose == pose

    def test_move_with_positive_yaw(self):
        pose = Pose(Point(1, 2), pi / 4)
        pose.move(sqrt(2))
        expected_pose = Pose(Point(2, 3), pi / 4)
        assert expected_pose == pose

    def test_move_with_negative_yaw(self):
        pose = Pose(Point(1, 2), -pi / 4)
        pose.move(sqrt(2))
        expected_pose = Pose(Point(0, 3), -pi / 4)
        assert expected_pose == pose

    def test_shift(self):
        pose = Pose(Point(1, 2), pi / 4)
        pose.shift(sqrt(2), pi / 4)
        expected_pose = Pose(Point(2, 3), pi / 2)
        assert expected_pose == pose

    def test_rotate(self):
        pose = Pose(Point(1, 2), pi / 4)
        pose.rotate(pi / 4)
        expected_pose = Pose(Point(1, 2), pi / 2)
        assert expected_pose == pose

    def test_calculate_angle_difference_positive(self):
        pose = Pose(Point(1, 2), pi / 4)
        goal = Point(2, 2)
        angle_difference = pose.calculate_angle_difference(goal)
        assert isclose(angle_difference, pi / 4)

    def test_calculate_angle_difference_negative(self):
        pose = Pose(Point(1, 2), pi / 4)
        goal = Point(1, 3)
        angle_difference = pose.calculate_angle_difference(goal)
        assert isclose(angle_difference, -pi / 4)
