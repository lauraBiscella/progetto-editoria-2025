
## Benvenuto in GuidaGreen! La tua guida Green

Se sei confuso, non sai dove girarti, ma ci tieni al pianeta noi possiamo aiutarti.

Questo libro digitale è qui per aiutare giovani come te a diventare abitanti consapevoli e più green in modo semplice e diretto.

<div style="text-align:center;">
  <img src="images/icon.webp" width="400"/>
</div>

<!-- Lettore audio nascosto -->
<audio id="audioPlayer">
  <source src="audio/audio_nature.mp4" type="audio/mp4">
</audio>

<!-- Contenitore per i pulsanti -->
<div class="audio-controls">
  <button class="audio-btn" onclick="playAudio()">▶️ Play</button>
  <button class="audio-btn" onclick="pauseAudio()">⏸️ Pausa</button>
  <button class="audio-btn" onclick="stopAudio()">⏹️ Stop</button>
</div>

<!-- Stile personalizzato solo per i pulsanti -->
<style>
  /* Contenitore dei pulsanti centrato */
  .audio-controls {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 20px;
  }

  /* Stile dei pulsanti audio */
  .audio-btn {
    background-color: #1f1f1f;
    color: #ffffff;
    border: none;
    padding: 15px 25px;
    font-size: 16px;
    border-radius: 10px;
    cursor: pointer;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    transition: transform 0.2s, background-color 0.3s;
  }

  /* Effetto hover */
  .audio-btn:hover {
    background-color: #333333;
    transform: scale(1.1);
  }

  /* Effetto click */
  .audio-btn:active {
    background-color: #555555;
    transform: scale(0.95);
  }
</style>

<!-- Script per il controllo audio -->
<script>
  var audio = document.getElementById("audioPlayer");

  function playAudio() {
    audio.play();
  }

  function pauseAudio() {
    audio.pause();
  }

  function stopAudio() {
    audio.pause();
    audio.currentTime = 0;
  }
</script>


- [Scopri di più](0_le_basi.md) sui temi del cambiamento climatico e dell'impatto ambientale.

- [Osserva](2_dati_statistici.md) alcuni dati ufficiali sull'inquinamento.

- [Fai un test](https://www.footprintcalculator.org/sponsor/FR/it) per scoprire il tuo impatto ambientale.

- [Scopri](3_gli_esperti.md) di chi fidarti leggendo articoli di esperti sulle tematiche ambientali.

- [Segui](4_stile_di_vita.md) le nostre proposte per una vita più Green.

- [Informati](1_il_digitale.md) su un tema molto importante al giorno d'oggi: L'inquinamento digitale. 

- [Sfida](5_green_challenge.md) te stesso nella Challenge Green

## Collabora con noi

In questo link troverai la [repo github](https://github.com/lauraBiscella/progetto-editoria-2025) attraverso la quale potrai collaborare con noi nel progetto di creazione di GuidaGreen. 

Oppure condividi le tue abitudini e conoscenze sui commenti delle nostre pagine social. 

