def get_curated_legends(day, month):
    legends = {
        (14, 2): [
            ("Frederick Douglass", "Born into slavery, he educated himself and became a voice for freedom."),
            ("You", "Your story doesn’t need permission to be legendary.")
        ],
        (24, 6): [
            ("Lionel Messi", "Diagnosed with a growth disorder, he became the greatest footballer ever."),
            ("You", "Limits only exist until you challenge them.")
        ],
        (27, 5): [
            ("Jawaharlal Nehru", "Faced imprisonment but shaped a nation."),
            ("You", "Pressure shapes diamonds.")
        ],
        (27, 8): [
            ("Mother Teresa", "A single life devoted to compassion changed millions."),
            ("You", "Kindness is also strength.")
        ],
        (21, 2): [
            ("Nina Simone", "Turned pain into music that moved generations."),
            ("You", "Your voice matters.")
        ],
        (24, 7): [
            ("Amelia Earhart", "She flew where no woman had before."),
            ("You", "You are allowed to go first.")
        ],
        (18, 7): [
            ("Nelson Mandela", "27 years imprisoned, yet he chose forgiveness."),
            ("You", "Your resilience is your power.")
        ],
        (5, 4): [
            ("Booker T. Washington", "Rose from poverty to become an educator."),
            ("You", "Growth starts wherever you are.")
        ],
        (28, 1): [
            ("Oprah Winfrey", "From hardship to influence."),
            ("You", "Your past does not define your ceiling.")
        ],
        (16, 10): [
            ("Oscar Wilde", "Misunderstood in his time, celebrated later."),
            ("You", "Timing does not reduce worth.")
        ],
    }

    return legends.get(
        (day, month),
        [
            ("No record before", "Perhaps the universe was waiting for you."),
            ("You", "Every legend starts somewhere.")
        ]
    )
