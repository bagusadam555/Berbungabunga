from satuprogram_level2 import sistem_identifikasi_losses_dataAIS
from duapredictor import sistem_predictor_losses_data
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama_kapal = request.form['nama_kapal']
        subsistem = request.form['subsistem']
        csv_file = request.files["csv_file"]
        # Lakukan sesuatu dengan data yang dikirim
        if int(subsistem)==1:
            jenis_sistem=sistem_identifikasi_losses_dataAIS(nama_kapal,csv_file)
            if jenis_sistem==2:
                message= f'Kesimpulan : Pada kapal {nama_kapal} ditemukan bahwa TELAH TERJADI losses data AIS selama lebih dari 2 jam'
            elif jenis_sistem==3:
                message= f'Kesimpulan : Pada kapal {nama_kapal} ditemukan bahwa TIDAK TERJADI losses data AIS selama lebih dari 2 jam'
            data={'message':message}
            return render_template('index.html',data=data)
        elif int(subsistem)==2:
            workbook,plot_image,plot_image2=sistem_predictor_losses_data(csv_file)
            return render_template('index.html', excel_data=workbook, plot_image=plot_image, plot_image2=plot_image2)
    elif request.method == 'GET':
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)