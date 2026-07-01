from datetime import datetime
from flask import Blueprint, redirect, render_template, request, url_for
from models import ClienteLocadora, Locacao, Veiculo, db

locadora_bp = Blueprint("locadora", __name__, url_prefix="/locadora")
dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def index():
    return redirect(url_for("locadora.index"))

@locadora_bp.route("/")
def index():
    locacoes = Locacao.listar_com_detalhes()
    return render_template("locadora/lista.html", locacoes=locacoes)

@locadora_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    clientes = ClienteLocadora.listar()
    veiculos = Veiculo.listar()

    if request.method == "POST":
        cliente_id = request.form.get("cliente_id")
        veiculo_id = request.form.get("veiculo_id")
        data_inicio_str = request.form.get("data_inicio")
        data_fim_str = request.form.get("data_fim")
        valor_total = request.form.get("valor_total")

        data_inicio = datetime.strptime(data_inicio_str, "%Y-%m-%d").date()
        data_fim = datetime.strptime(data_fim_str, "%Y-%m-%d").date()

        nova_locacao = Locacao(
            cliente_id=int(cliente_id),
            veiculo_id=int(veiculo_id),
            data_inicio=data_inicio,
            data_fim=data_fim,
            valor_total=float(valor_total)
        )

        db.session.add(nova_locacao)
        db.session.commit()
        return redirect(url_for("locadora.index"))

    return render_template(
        "locadora/formulario.html",
        clientes=clientes,
        veiculos=veiculos,
    )