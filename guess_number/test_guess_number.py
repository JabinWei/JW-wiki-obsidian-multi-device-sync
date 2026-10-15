"""
单元测试：猜数字游戏
运行方式：pytest test_guess_number.py -v
分步运行：pytest -m "taskno=N" -v （N 是任务号）
"""

import pytest
from unittest.mock import patch
from guess_number_game import (
    generate_number,
    get_user_guess,
    play_one_round
)


@pytest.mark.task(taskno=1)
class TestGenerateNumber:
    """任务 1：测试 generate_number 函数"""

    def test_returns_integer_in_range(self):
        """测试返回值是指定范围内的整数"""
        for _ in range(100):  # 多次测试避免概率问题
            num = generate_number(0, 100)
            assert isinstance(num, int)
            assert 0 <= num <= 100

    def test_custom_range_works(self):
        """测试自定义范围也能正常工作"""
        for _ in range(100):
            num = generate_number(10, 20)
            assert 10 <= num <= 20


@pytest.mark.task(taskno=2)
class TestGetUserGuess:
    """任务 2：测试 get_user_guess 函数"""

    @patch('builtins.input', side_effect=['50'])
    def test_valid_input_returns_integer(self, mock_input):
        """测试合法输入返回正确整数"""
        result = get_user_guess()
        assert result == 50
        mock_input.assert_called_once()

    @patch('builtins.input', side_effect=['abc', 'def', '42'])
    def test_invalid_input_retries(self, mock_input):
        """测试非法输入会一直要求重试，直到拿到合法数字"""
        result = get_user_guess()
        assert result == 42
        # 调用了三次 input，说明重试了两次
        assert mock_input.call_count == 3

    @patch('builtins.input', side_effect=['-1'])
    def test_minus_one_returns_immediately(self, mock_input):
        """测试输入 -1 直接返回，不做范围检查"""
        result = get_user_guess()
        assert result == -1
        mock_input.assert_called_once()


@pytest.mark.task(taskno=3)
class TestPlayOneRound:
    """任务 3：测试 play_one_round 函数"""

    @patch('guess_number_game.get_user_guess', side_effect=[50, 25, 12, 42])
    def test_correct_guess_returns_guess_count(self, mock_guess):
        """测试猜对了返回正确的猜测次数"""
        # mock random 固定生成 42
        with patch('guess_number_game.generate_number', return_value=42):
            count = play_one_round()
            assert count == 4
            assert mock_guess.call_count == 4

    @patch('guess_number_game.get_user_guess', return_value=-1)
    def test_user_exits_returns_zero(self, mock_guess):
        """测试用户中途退出返回 0"""
        with patch('guess_number_game.generate_number', return_value=42):
            count = play_one_round()
            assert count == 0
            assert mock_guess.called_once()

    @patch('guess_number_game.get_user_guess', side_effect=[10, 20, 30, 40, 50, 42])
    @patch('builtins.print')
    def test_prints_prompts_correctly(self, mock_print, mock_guess):
        """测试游戏过程正确打印提示信息"""
        with patch('guess_number_game.generate_number', return_value=42):
            play_one_round()
            # 至少会打印 "太小了" / "太大了" 几次，最后打印 "恭喜猜对了"
            assert any("恭喜" in str(call) for call in mock_print.call_args_list)
            assert any("太小" in str(call) for call in mock_print.call_args_list)
