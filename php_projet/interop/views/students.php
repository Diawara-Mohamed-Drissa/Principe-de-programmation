<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Liste des étudiants</title>
    <link rel="stylesheet" href="interop/assets/style.css">
</head>
<body>

<h1>Liste des étudiants</h1>

<p>
    <a href="index.php?action=create">➕ Ajouter un étudiant</a>
</p>

<form method="GET" action="index.php">
    <input type="hidden" name="action" value="search">
    <input type="number" name="id" placeholder="ID étudiant" required>
    <button type="submit">Rechercher</button>
</form>

<hr>

<?php foreach ($students as $student): ?>
    <p>
        <?= $student['name'] ?> (<?= $student['age'] ?> ans)
        —
        <a href="index.php?action=show&id=<?= $student['id'] ?>">Voir</a>
        —
        <a href="index.php?action=edit&id=<?= $student['id'] ?>">Modifier</a>
        —
        <a href="index.php?action=delete&id=<?= $student['id'] ?>" onclick="return confirm('Supprimer ?');">Supprimer</a>
    </p>
<?php endforeach; ?>

</body>
</html>