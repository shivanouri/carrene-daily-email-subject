from easycli import Argument, Root, SubCommand

from subjectsgeneration.subjects.get_subject import get_daily_subject


class SubjectCommand(SubCommand):
    __command__ = 'subject'
    __arguments__ = [
        Argument(
            '-t', '--team',
            required=True,
            default='',
            help='Your team name to appear in generated subject.'
        ),
    ]

    def __call__(self, args):
        if args.team:
            team_name = args.team
            print(get_daily_subject(team_name))


class Main(Root):
    __help__ = 'Daily Report Subject Generator'
    __completion__ = True

    __arguments__ = [
        SubjectCommand
    ]


if __name__ == '__main__':
    Main()
