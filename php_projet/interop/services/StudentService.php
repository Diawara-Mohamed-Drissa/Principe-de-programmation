<?php

class StudentService
{
    private static function request(string $method, string $endpoint, ?array $data = null)
    {
        $url = rtrim(API_BASE_URL, '/') . $endpoint;

        $options = [
            'http' => [
                'method' => $method,
                'header' => "Content-Type: application/json\r\nAccept: application/json\r\n",
                'ignore_errors' => true
            ]
        ];

        if ($data !== null) {
            $options['http']['content'] = json_encode($data);
        }

        $context = stream_context_create($options);
        $response = file_get_contents($url, false, $context);

        if ($response === false) {
            return null;
        }

        return json_decode($response, true);
    }

    public static function getAllStudents()
    {
        return self::request('GET', '/students');
    }

    public static function getStudentById(int $id)
    {
        return self::request('GET', '/students/' . $id);
    }

    public static function addStudent(array $student)
    {
        return self::request('POST', '/students', $student);
    }

    public static function updateStudent(int $id, array $student)
    {
        return self::request('PUT', '/students/' . $id, $student);
    }

    public static function deleteStudent(int $id)
    {
        return self::request('DELETE', '/students/' . $id);
    }
}