<?php
require_once __DIR__ . '/../services/StudentService.php';

class StudentController
{
    public static function index()
    {
        $students = StudentService::getAllStudents();
        if (!is_array($students)) $students = [];
        require __DIR__ . '/../views/students.php';
    }

    public static function show(int $id)
    {
        $student = StudentService::getStudentById($id);
        require __DIR__ . '/../views/student_show.php';
    }

    public static function create()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $data = [
                'name' => $_POST['name'] ?? '',
                'age'  => (int)($_POST['age'] ?? 0),
            ];
            StudentService::addStudent($data);
            header('Location: index.php?action=list');
            exit;
        }

        $mode = 'create';
        $student = ['name' => '', 'age' => ''];
        require __DIR__ . '/../views/student_form.php';
    }

    public static function edit(int $id)
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $data = [
                'name' => $_POST['name'] ?? '',
                'age'  => (int)($_POST['age'] ?? 0),
            ];
            StudentService::updateStudent($id, $data);
            header('Location: index.php?action=list');
            exit;
        }

        $mode = 'edit';
        $student = StudentService::getStudentById($id);
        require __DIR__ . '/../views/student_form.php';
    }

    public static function delete(int $id)
    {
        StudentService::deleteStudent($id);
        header('Location: index.php?action=list');
        exit;
    }

    public static function searchById()
    {
        $id = (int)($_GET['id'] ?? 0);
        if ($id > 0) {
            header('Location: index.php?action=show&id=' . $id);
            exit;
        }
        header('Location: index.php?action=list');
        exit;
    }
}