<?php
require_once __DIR__ . '/interop/config/config.php';
require_once __DIR__ . '/interop/controllers/StudentController.php';

$action = $_GET['action'] ?? 'list';
$id = isset($_GET['id']) ? (int)$_GET['id'] : 0;

switch ($action) {
    case 'list':
        StudentController::index();
        break;

    case 'show':
        StudentController::show($id);
        break;

    case 'create':
        StudentController::create();
        break;

    case 'edit':
        StudentController::edit($id);
        break;

    case 'delete':
        StudentController::delete($id);
        break;

    case 'search':
        StudentController::searchById();
        break;

    default:
        StudentController::index();
        break;
}