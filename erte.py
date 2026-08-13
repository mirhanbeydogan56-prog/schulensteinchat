<!DOCTYPE html>
<html lang="tr">

<head>

    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>💕 Senin İçin</title>


    <style>

        * {
            box-sizing: border-box;
        }


        html,
        body {
            margin: 0;
            width: 100%;
            min-height: 100%;
        }


        body {

            min-height: 100vh;

            font-family:
                Arial,
                sans-serif;

            color: white;

            overflow-x: hidden;

            background:
                radial-gradient(
                    circle at 50% 20%,
                    #5c0927 0%,
                    #300015 35%,
                    #130008 100%
                );

        }


        /* =========================
           ARKA PLAN KALPLERİ
        ========================= */

        .background-heart {

            position: fixed;

            color:
                rgba(
                    255,
                    77,
                    109,
                    0.12
                );

            pointer-events: none;

            animation:
                backgroundFloat
                linear
                infinite;

            z-index: 0;

        }


        @keyframes backgroundFloat {

            0% {

                transform:
                    translateY(110vh)
                    rotate(0deg);

                opacity: 0;

            }

            20% {

                opacity: 1;

            }

            100% {

                transform:
                    translateY(-15vh)
                    rotate(360deg);

                opacity: 0;

            }

        }


        /* =========================
           ANA ALAN
        ========================= */

        .page {

            position: relative;

            z-index: 2;

            width: 100%;

            min-height: 100vh;

            padding:
                25px
                20px
                50px;

        }


        .title {

            text-align: center;

            margin:
                10px
                0
                5px;

            color:
                #ff9fb2;

            font-size:
                clamp(
                    28px,
                    6vw,
                    48px
                );

            text-shadow:
                0 0 20px
                rgba(
                    255,
                    77,
                    109,
                    0.5
                );

        }


        .subtitle {

            text-align: center;

            color:
                #d895a5;

            margin-bottom:
                20px;

        }


        /* =========================
           OYUNCU BİLGİSİ
        ========================= */

        .player-bar {

            width: 100%;

            max-width: 900px;

            margin:
                0 auto
                20px;

            display: flex;

            justify-content: center;

            flex-wrap: wrap;

            gap: 10px;

        }


        .player {

            background:
                rgba(
                    50,
                    0,
                    20,
                    0.8
                );

            border:
                1px solid
                rgba(
                    255,
                    143,
                    163,
                    0.2
                );

            border-radius:
                50px;

            padding:
                9px
                15px;

            color:
                #d9a1ae;

            transition:
                0.25s;

        }


        .player.active {

            border-color:
                #ff4d6d;

            color:
                white;

            box-shadow:
                0 0 15px
                rgba(
                    255,
                    77,
                    109,
                    0.3
                );

        }


        .player-dot {

            display:
                inline-block;

            width:
                9px;

            height:
                9px;

            border-radius:
                50%;

            background:
                #666;

            margin-right:
                5px;

        }


        .player.active
        .player-dot {

            background:
                #4dffb8;

            box-shadow:
                0 0 8px
                #4dffb8;

        }


        /* =========================
           OYUN ALANI
        ========================= */

        .game-area {

            position: relative;

            width: 100%;

            max-width: 900px;

            min-height:
                600px;

            margin:
                0 auto;

            background:
                rgba(
                    20,
                    0,
                    10,
                    0.55
                );

            border:
                1px solid
                rgba(
                    255,
                    77,
                    109,
                    0.18
                );

            border-radius:
                30px;

            box-shadow:
                0 20px 70px
                rgba(
                    0,
                    0,
                    0,
                    0.4
                );

            overflow:
                hidden;

        }


        /* =========================
           STRES TOPU
        ========================= */

        .ball-container {

            position: absolute;

            left: 50%;

            top: 48%;

            transform:
                translate(
                    -50%,
                    -50%
                );

            width:
                260px;

            height:
                260px;

            display:
                flex;

            justify-content:
                center;

            align-items:
                center;

            z-index: 10;

        }


        .stress-ball {

            width:
                210px;

            height:
                210px;

            border-radius:
                48% 52%
                55% 45% /
                50% 45%
                55% 50%;

            cursor:
                pointer;

            user-select:
                none;

            touch-action:
                none;

            background:

                radial-gradient(
                    circle at 30% 25%,
                    #ff9db0,
                    #ff5575 35%,
                    #d91f4e 70%,
                    #870024 100%
                );

            box-shadow:

                inset
                -18px
                -20px
                35px
                rgba(
                    80,
                    0,
                    20,
                    0.5
                ),

                inset
                15px
                12px
                20px
                rgba(
                    255,
                    255,
                    255,
                    0.25
                ),

                0
                20px
                40px
                rgba(
                    0,
                    0,
                    0,
                    0.4
                );

            transition:

                transform
                0.15s
                ease,

                border-radius
                0.15s
                ease;

            display:
                flex;

            align-items:
                center;

            justify-content:
                center;

            font-size:
                55px;

        }


        .stress-ball:hover {

            transform:
                scale(1.04);

        }


        .stress-ball.pressed {

            transform:
                scale(
                    1.16,
                    0.78
                );

            border-radius:
                55% 45%
                65% 35% /
                40% 55%
                45% 60%;

        }


        .stress-ball.popping {

            animation:
                ballPop
                0.55s
                ease
                forwards;

        }


        @keyframes ballPop {

            0% {

                transform:
                    scale(
                        1.1,
                        0.8
                    );

            }

            35% {

                transform:
                    scale(
                        1.35,
                        0.65
                    );

            }

            60% {

                transform:
                    scale(
                        0.8
                    );

                opacity:
                    0.7;

            }

            100% {

                transform:
                    scale(
                        0
                    );

                opacity:
                    0;

            }

        }


        /* =========================
           BALON GİBİ GERİ GELME
        ========================= */

        .stress-ball.returning {

            animation:
                ballReturn
                0.6s
                cubic-bezier(
                    .2,
                    .8,
                    .3,
                    1.2
                );

        }


        @keyframes ballReturn {

            0% {

                transform:
                    scale(0);

            }

            60% {

                transform:
                    scale(1.15);

            }

            100% {

                transform:
                    scale(1);

            }

        }


        /* =========================
           KALPLER
        ========================= */

        .heart {

            position:
                absolute;

            left:
                50%;

            top:
                50%;

            font-size:
                30px;

            cursor:
                pointer;

            user-select:
                none;

            z-index:
                8;

            filter:
                drop-shadow(
                    0
                    5px
                    8px
                    rgba(
                        0,
                        0,
                        0,
                        0.35
                    )
                );

            animation:
                heartFly
                1.3s
                cubic-bezier(
                    .15,
                    .8,
                    .25,
                    1
                )
                forwards;

            transform-origin:
                center;

        }


        .heart:hover {

            filter:
                drop-shadow(
                    0
                    0
                    10px
                    #62d9ff
                );

        }


        .heart.squish {

            animation:
                heartSquish
                0.4s
                ease
                forwards;

            pointer-events:
                none;

        }


        @keyframes heartFly {

            0% {

                transform:
                    translate(
                        -50%,
                        -50%
                    )
                    scale(0.2)
                    rotate(0deg);

                opacity:
                    0;

            }

            25% {

                opacity:
                    1;

            }

            100% {

                transform:
                    translate(
                        calc(
                            -50% +
                            var(--x)
                        ),
                        calc(
                            -50% +
                            var(--y)
                        )
                    )
                    scale(
                        var(--scale)
                    )
                    rotate(
                        var(--rotate)
                    );

                opacity:
                    1;

            }

        }


        @keyframes heartSquish {

            0% {

                transform:
                    scale(1);

                opacity:
                    1;

            }

            40% {

                transform:
                    scale(
                        1.4,
                        0.45
                    );

            }

            100% {

                transform:
                    scale(
                        0
                    );

                opacity:
                    0;

            }

        }


        /* =========================
           PATLAMA PARÇACIKLARI
        ========================= */

        .particle {

            position:
                absolute;

            left:
                50%;

            top:
                50%;

            width:
                8px;

            height:
                8px;

            border-radius:
                50%;

            pointer-events:
                none;

            animation:
                particleFly
                0.9s
                ease-out
                forwards;

            z-index:
                7;

        }


        @keyframes particleFly {

            0% {

                transform:
                    translate(
                        -50%,
                        -50%
                    )
                    scale(1);

                opacity:
                    1;

            }

            100% {

                transform:
                    translate(
                        calc(
                            -50% +
                            var(--px)
                        ),
                        calc(
                            -50% +
                            var(--py)
                        )
                    )
                    scale(0);

                opacity:
                    0;

            }

        }


        /* =========================
           TALİMAT
        ========================= */

        .hint {

            position:
                absolute;

            bottom:
                25px;

            left:
                50%;

            transform:
                translateX(-50%);

            width:
                calc(
                    100% - 40px
                );

            text-align:
                center;

            color:
                #b9798a;

            font-size:
                14px;

            z-index:
                3;

        }


        .hint strong {

            color:
                #ff8fa3;

        }


        /* =========================
           PATLAMA YAZISI
        ========================= */

        .boom {

            position:
                absolute;

            left:
                50%;

            top:
                48%;

            transform:
                translate(
                    -50%,
                    -50%
                )
                scale(0);

            color:
                #ffffff;

            font-size:
                55px;

            font-weight:
                900;

            text-shadow:
                0
                0
                20px
                #35cfff;

            pointer-events:
                none;

            z-index:
                20;

            opacity:
                0;

        }


        .boom.show {

            animation:
                boomAnimation
                0.8s
                ease
                forwards;

        }


        @keyframes boomAnimation {

            0% {

                transform:
                    translate(
                        -50%,
                        -50%
                    )
                    scale(0);

                opacity:
                    0;

            }

            30% {

                transform:
                    translate(
                        -50%,
                        -50%
                    )
                    scale(1.3);

                opacity:
                    1;

            }

            70% {

                transform:
                    translate(
                        -50%,
                        -50%
                    )
                    scale(1);

                opacity:
                    1;

            }

            100% {

                transform:
                    translate(
                        -50%,
                        -50%
                    )
                    scale(1.4);

                opacity:
                    0;

            }

        }


        /* =========================
           RESET
        ========================= */

        .reset-btn {

            position:
                absolute;

            top:
                18px;

            right:
                18px;

            padding:
                9px 14px;

            border:
                1px solid
                rgba(
                    255,
                    143,
                    163,
                    0.2
                );

            border-radius:
                12px;

            background:
                rgba(
                    40,
                    0,
                    15,
                    0.7
                );

            color:
                #d993a4;

            cursor:
                pointer;

            z-index:
                30;

        }


        .reset-btn:hover {

            background:
                #ff4d6d;

            color:
                white;

        }


        /* =========================
           MOBİL
        ========================= */

        @media (
            max-width: 600px
        ) {

            .page {

                padding:
                    15px
                    10px
                    30px;

            }


            .game-area {

                min-height:
                    570px;

                border-radius:
                    25px;

            }


            .ball-container {

                width:
                    230px;

                height:
                    230px;

            }


            .stress-ball {

                width:
                    180px;

                height:
                    180px;

                font-size:
                    45px;

            }


            .heart {

                font-size:
                    27px;

            }


            .hint {

                bottom:
                    20px;

            }


            .boom {

                font-size:
                    45px;

            }

        }

    </style>

</head>


<body>


    <!-- =========================
         ARKA PLAN
    ========================= -->

    <div id="background"></div>


    <main class="page">


        <h1 class="title">

            💕 Senin İçin 💕

        </h1>


        <div class="subtitle">

            Biraz stresini atalım... 😌

        </div>


        <!-- OYUNCULAR -->

        <div class="player-bar">

            <div
                class="player active"
                id="player1"
            >

                <span
                    class="player-dot"
                ></span>

                Oyuncu 1

            </div>


            <div
                class="player"
                id="player2"
            >

                <span
                    class="player-dot"
                ></span>

                Oyuncu 2

            </div>


            <div
                class="player"
                id="player3"
            >

                <span
                    class="player-dot"
                ></span>

                Oyuncu 3

            </div>

        </div>


        <!-- =========================
             OYUN
        ========================= -->

        <section class="game-area">


            <button
                class="reset-btn"
                onclick="resetGame()"
            >

                ↻

            </button>


            <div
                class="ball-container"
                id="ballContainer"
            >

                <div
                    class="stress-ball"
                    id="stressBall"
                >

                    💗

                </div>

            </div>


            <div
                class="boom"
                id="boom"
            >

                BOOM! 💙

            </div>


            <div class="hint">

                <strong>Basılı tut</strong>
                ve stres topunu ez...

                <br>

                Bırakınca ne çıkacağını gör
                💙

            </div>


        </section>


    </main>


    <script>

        /* =========================
           ELEMENTLER
        ========================= */

        const ball =
            document.getElementById(
                "stressBall"
            );


        const ballContainer =
            document.getElementById(
                "ballContainer"
            );


        const gameArea =
            document.querySelector(
                ".game-area"
            );


        const boom =
            document.getElementById(
                "boom"
            );


        /* =========================
           BASILI TUTMA
        ========================= */

        let isPressing =
            false;

        let pressTimer =
            null;

        let hasPopped =
            false;


        function startPress(
            event
        ) {

            event.preventDefault();


            if (isPressing)
                return;


            isPressing =
                true;


            hasPopped =
                false;


            ball.classList.add(
                "pressed"
            );


            /*
             * Biraz basılı tutulduktan
             * sonra top hazır hale geliyor.
             */

            pressTimer =
                setTimeout(
                    function() {

                        if (
                            isPressing
                        ) {

                            ball.style
                                .filter =
                                "brightness(1.2)";

                        }

                    },
                    500
                );

        }


        function endPress(
            event
        ) {

            if (
                !isPressing
            )
                return;


            isPressing =
                false;


            clearTimeout(
                pressTimer
            );


            ball.classList.remove(
                "pressed"
            );


            /*
             * Bırakınca patlat.
             */

            if (
                !hasPopped
            ) {

                hasPopped =
                    true;

                popBall();

            }

        }


        ball.addEventListener(
            "pointerdown",
            startPress
        );


        ball.addEventListener(
            "pointerup",
            endPress
        );


        ball.addEventListener(
            "pointercancel",
            endPress
        );


        ball.addEventListener(
            "pointerleave",
            function(event) {

                /*
                 * Mouse ile dışarı çıkınca
                 * bırakılmış sayıyoruz.
                 */

                if (
                    event.pointerType ===
                    "mouse" &&
                    isPressing
                ) {

                    endPress(
                        event
                    );

                }

            }
        );


        /* =========================
           TOPU PATLAT
        ========================= */

        function popBall() {

            ball.classList.add(
                "popping"
            );


            /*
             * BOOM yazısı
             */

            boom.classList.remove(
                "show"
            );


            void boom.offsetWidth;


            boom.classList.add(
                "show"
            );


            /*
             * Mavi kalpler
             */

            createHearts();


            /*
             * Parçacıklar
             */

            createParticles();


            /*
             * Topu geri getir
             */

            setTimeout(
                function() {

                    ball.classList.remove(
                        "popping"
                    );


                    ball.style.filter =
                        "";


                    ball.classList.add(
                        "returning"
                    );


                    setTimeout(
                        function() {

                            ball.classList.remove(
                                "returning"
                            );

                        },
                        600
                    );

                },
                550
            );

        }


        /* =========================
           MAVİ KALPLER
        ========================= */

        function createHearts() {

            const count =
                10 +
                Math.floor(
                    Math.random() * 9
                );


            for (
                let i = 0;
                i < count;
                i++
            ) {

                const heart =
                    document.createElement(
                        "div"
                    );


                heart.className =
                    "heart";


                heart.textContent =
                    Math.random() < 0.7
                        ? "💙"
                        : "🩵";


                /*
                 * Rastgele yön
                 */

                const x =
                    (
                        Math.random() *
                        500
                    ) - 250;


                const y =
                    (
                        Math.random() *
                        430
                    ) - 300;


                const scale =
                    (
                        0.7 +
                        Math.random() *
                        0.9
                    );


                const rotate =
                    (
                        Math.random() *
                        80
                    ) - 40;


                heart.style.setProperty(
                    "--x",
                    x + "px"
                );


                heart.style.setProperty(
                    "--y",
                    y + "px"
                );


                heart.style.setProperty(
                    "--scale",
                    scale
                );


                heart.style.setProperty(
                    "--rotate",
                    rotate + "deg"
                );


                heart.style.animationDelay =
                    (
                        Math.random() *
                        0.12
                    ) + "s";


                gameArea.appendChild(
                    heart
                );


                /*
                 * Kalbe dokununca ez
                 */

                heart.addEventListener(
                    "pointerdown",
                    function(event) {

                        event.stopPropagation();

                        squishHeart(
                            heart
                        );

                    }
                );


                /*
                 * 5 saniye sonra
                 * kendisi kaybolsun.
                 */

                setTimeout(
                    function() {

                        if (
                            heart.isConnected
                        ) {

                            squishHeart(
                                heart
                            );

                        }

                    },
                    5000
                );

            }

        }


        /* =========================
           KALP EZME
        ========================= */

        function squishHeart(
            heart
        ) {

            if (
                heart.classList.contains(
                    "squish"
                )
            ) {

                return;

            }


            heart.classList.add(
                "squish"
            );


            setTimeout(
                function() {

                    heart.remove();

                },
                400
            );

        }


        /* =========================
           PARÇACIK
        ========================= */

        function createParticles() {

            const colors = [

                "#48d8ff",
                "#72e5ff",
                "#ffffff",
                "#4da6ff",
                "#ff8fa3"

            ];


            for (
                let i = 0;
                i < 28;
                i++
            ) {

                const particle =
                    document.createElement(
                        "div"
                    );


                particle.className =
                    "particle";


                particle.style.background =
                    colors[
                        Math.floor(
                            Math.random() *
                            colors.length
                        )
                    ];


                const angle =
                    Math.random() *
                    Math.PI *
                    2;


                const distance =
                    80 +
                    Math.random() *
                    220;


                const px =
                    Math.cos(angle) *
                    distance;


                const py =
                    Math.sin(angle) *
                    distance;


                particle.style.setProperty(
                    "--px",
                    px + "px"
                );


                particle.style.setProperty(
                    "--py",
                    py + "px"
                );


                gameArea.appendChild(
                    particle
                );


                setTimeout(
                    function() {

                        particle.remove();

                    },
                    1000
                );

            }

        }


        /* =========================
           ARKA PLAN KALPLERİ
        ========================= */

        function createBackgroundHeart() {

            const heart =
                document.createElement(
                    "div"
                );


            heart.className =
                "background-heart";


            heart.textContent =
                Math.random() < 0.5
                    ? "♡"
                    : "♥";


            heart.style.left =
                Math.random() *
                100 +
                "vw";


            heart.style.fontSize =
                (
                    15 +
                    Math.random() *
                    35
                ) +
                "px";


            heart.style.animationDuration =
                (
                    7 +
                    Math.random() *
                    8
                ) +
                "s";


            document.body.appendChild(
                heart
            );


            setTimeout(
                function() {

                    heart.remove();

                },
                16000
            );

        }


        setInterval(
            createBackgroundHeart,
            900
        );


        /* =========================
           RESET
        ========================= */

        function resetGame() {

            document
                .querySelectorAll(
                    ".heart, .particle"
                )
                .forEach(
                    function(element) {

                        element.remove();

                    }
                );


            ball.classList.remove(
                "popping",
                "returning",
                "pressed"
            );


            ball.style.filter =
                "";


            boom.classList.remove(
                "show"
            );

        }


    </script>


</body>

</html>
