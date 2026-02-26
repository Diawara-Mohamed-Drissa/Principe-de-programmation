<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Détail étudiant</title>
    <link rel="stylesheet" href="interop/assets/style.css">
</head>
<body>

<h1>Détail étudiant</h1>

<?php if (!$student || !isset($student['id'])): ?>
    <p>Étudiant introuvable.</p>
<?php else: ?>
    <p><strong>ID :</strong> <?= $student['id'] ?></p>
    <p><strong>Nom :</strong> <?= $student['name'] ?></p>
    <p><strong>Âge :</strong> <?= $student['age'] ?> ans</p>
<?php endif; ?>

<p><a href="index.php?action=list">⬅ Retour</a></p>

</body>
</html>