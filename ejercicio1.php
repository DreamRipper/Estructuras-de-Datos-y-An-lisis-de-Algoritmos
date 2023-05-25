<?php

$votos = array_fill(1, 30, 0); 

for ($i = 0; $i < 5000; $i++) {
    $candidato = rand(1, 30); 
    $votos[$candidato]++; 
}

arsort($votos);

foreach ($votos as $candidato => $voto_count) {
    echo "<br>Candidato $candidato: $voto_count votes\n";
}

?>