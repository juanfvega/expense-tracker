import argparse
from .logic import add_expense, list_expenses, summarize_expenses, delete_expense

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # "add" subcommand
    add_parser = subparsers.add_parser("add", help="Agregar un nuevo gasto")
    add_parser.add_argument("--amount", type=float, required=True, help="Monto del gasto")
    add_parser.add_argument("--description", type=str, required=True, help="Descripción")
    add_parser.add_argument("--category", type=str, required=True, help="Categoría")

    # "list" subcommand
    list_parser = subparsers.add_parser("list", help="Listar todos los gastos")

    # "summary" subcommand
    summary_parser = subparsers.add_parser("summary", help="Resumen de gastos")
    summary_parser.add_argument("--month", type=int, help="Mes numérico para resumen mensual (1-12)")

    # "delete" subcommand
    del_parser = subparsers.add_parser("delete", help="Eliminar un gasto por ID")
    del_parser.add_argument("--id", type=int, required=True, help="ID del gasto a eliminar (de la lista)")

    args = parser.parse_args()
    if args.command == "add":
        expense = add_expense(args.amount, args.description, args.category)
        print(f"Gasto agregado: {expense.amount} {expense.description} [{expense.category}]")
    elif args.command == "list":
        expenses = list_expenses()
        if not expenses:
            print("No hay gastos registrados.")
        else:
            for idx, e in enumerate(expenses, 1):
                print(f"{idx}. {e.date[:10]} - {e.amount} - {e.description} [{e.category}]")
    elif args.command == "summary":
        if args.month:
            total = summarize_expenses(month=args.month)
            print(f"Total expenses for month {args.month}: ${total:.2f}")
        else:
            total = summarize_expenses()
            print(f"Total expenses: ${total:.2f}")
    elif args.command == "delete":
        success = delete_expense(args.id)
        if success:
            print("Expense deleted successfully")
        else:
            print("ID inválido. No se ha eliminado ningún gasto.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()