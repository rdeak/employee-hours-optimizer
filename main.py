import gurobipy as gp
from gurobipy import GRB


def main() -> None:
    with gp.Env() as env:
        with gp.Model("employees_schedule", env=env) as model:
            try:
                x = model.addVar(vtype=GRB.BINARY, name="x")
                y = model.addVar(vtype=GRB.BINARY, name="y")
                z = model.addVar(vtype=GRB.BINARY, name="z")

                model.addConstr(x + 2 * y + 3 * z <= 4, "c0")

                model.setObjective(x + y + 2 * z, GRB.MAXIMIZE)

                model.optimize()

                for v in model.getVars():
                    print("%s %g" % (v.VarName, v.X))

                print("Obj: %g" % model.ObjVal)

            except gp.GurobiError as e:
                print(f"Gurobi error code {e.errno}: {e}")
            except AttributeError:
                print("Encountered an attribute error")


if __name__ == "__main__":
    main()
