<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title><?= ($mode === 'edit') ? 'Modifier' : 'Ajouter' ?></title>
    <link rel="stylesheet" href="interop/assets/style.css">
</head>
<body>

<h1><?= ($mode === 'edit') ? 'Modifier' : 'Ajouter' ?> un étudiant</h1>

<form method="POST" action="index.php?action=<?= ($mode === 'edit') ? 'edit&id=' . ($student['id'] ?? 0) : 'create' ?>">
    <label>Nom :</label><br>
    <input type="text" name="name" value="<?= $student['name'] ?? '' ?>" required><br><br>

    <label>Âge :</label><br>
    <input type="number" name="age" value="<?= $student['age'] ?? '' ?>" required><br><br>

    <button type="submit">Enregistrer</button>
</form>

<p><a href="index.php?action=list">⬅ Retour</a></p>

</body>
</html>