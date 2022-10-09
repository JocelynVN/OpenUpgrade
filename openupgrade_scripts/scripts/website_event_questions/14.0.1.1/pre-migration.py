from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
<<<<<<< HEAD
=======
    openupgrade.rename_models(env.cr, [("event.answer", "event.question.answer")])

>>>>>>> refs/remotes/OCA/14.0
    openupgrade.rename_tables(
        env.cr,
        [("event_answer", "event_question_answer")],
    )

    openupgrade.rename_fields(
        env,
        [
            (
                "event.registration.answer",
                "event_registration_answer",
                "event_answer_id",
                "value_answer_id",
            ),
            (
                "event.registration.answer",
                "event_registration_answer",
                "event_registration_id",
                "registration_id",
            ),
        ],
    )
