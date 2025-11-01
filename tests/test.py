"""
Тесты для лабы
"""
import unittest
from unittest.mock import patch, MagicMock

class TestCommand(unittest.TestCase):
    @patch('builtins.print')
    @patch('os.listdir')
    @patch('os.path.exists')
    def test_ls(self, mock_exist, mock_list, mock_print):
        """Тест ls + """
        mock_exist.return_value = True
        mock_list.return_value = ['file', 'file2','file3']
        from LABA2.src.power import ls
        ls(1, ".")
        mock_print.assert_any_call('file')
        mock_print.assert_any_call('file2')
        mock_print.assert_any_call('file3')
    @patch('builtins.print')
    @patch('os.path.exists')
    def test_ls_directory_not_found(self, mock_exist, mock_print):
        """Тест ls c фейком"""
        mock_exist.return_value = False
        from LABA2.src.power import ls
        result = ls(1, "C:\\fake")

        self.assertFalse(result[0])
        mock_print.assert_called_with("Каталог не существует: C:\\fake")

    @patch('os.chdir')
    @patch('os.path.exists')
    def test_cd_success(self, mock_exist, mock_chdir):
        """Тест cd +"""
        mock_exist.return_value = True
        from LABA2.src.power import cd
        result = cd("/valid/path")
        mock_chdir.assert_called_with("/valid/path")
        self.assertEqual(result, None)
    @patch('shutil.copy')
    @patch('os.path.isdir')
    def test_cp(self, mock_isdir, mock_copy):
        """Тест сp +"""
        mock_isdir.return_value = False
        from LABA2.src.power import cp
        cp(0, "otsuda", "suda")
        mock_copy.assert_called_with("otsuda", "suda")

    @patch('shutil.copytree')
    @patch('os.path.isdir')
    def test_cp_r(self, mock_isdir, mock_copytree):
        """Тест cp -r"""
        mock_isdir.return_value = True
        from LABA2.src.power import cp
        cp("-r", "otsuda", "suda")
        mock_copytree.assert_called_with("otsuda", "suda", dirs_exist_ok=True)
    @patch('shutil.move')
    def test_mv(self, mock_mv):
        """Тест mv +"""
        from LABA2.src.power import mv
        mv("otsuda", "suda")
        mock_mv.assert_called_with("otsuda", "suda")
    @patch('os.remove')
    def test_rm(self, mock_rm):
        """Тест rm"""
        from LABA2.src.power import rm
        rm(1, "file.txt")
        mock_rm.assert_called_with("file.txt")
    @patch('shutil.rmtree')
    def test_rm_r(self, mock_rmtree):
        """Тест rm -r"""
        from LABA2.src.power import rm
        rm("-r", "directory")
        mock_rmtree.assert_called_once()

    @patch('shutil.make_archive')
    def test_zip(self, mock_zip):
        """Тест zip """
        from LABA2.src.power import zip
        zip("archive", "folder")
        mock_zip.assert_called_with('archive', 'zip', 'folder')
    @patch('shutil.unpack_archive')
    def test_unzip_command(self, mock_unzip):
        """Тест unzip"""
        from LABA2.src.power import unzip
        unzip("archive.zip")
        mock_unzip.assert_called_with("archive.zip")
    @patch('builtins.print')
    @patch('builtins.open')
    def test_grep_file(self, mock_open, mock_print):
        """Тест grep"""
        mock = MagicMock()
        mock.__enter__.return_value = mock
        mock.__iter__.return_value = ["test str", "str"]
        mock_open.return_value = mock
        mock_pattern = MagicMock()
        mock_pattern.search.side_effect = [True, False]
        from LABA2.src.power import grep
        grep(1, mock_pattern, "file.txt")
        mock_print.assert_called_with("file.txt:1: test line")
if __name__ == '__main__':
    unittest.main()
