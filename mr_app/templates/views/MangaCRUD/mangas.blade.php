@extends('layouts.app')


@section('conteudo')


  <!-- ***** Main Banner Area End ***** -->
<section class="apply-now" id="apply" >
    <div class="container">
      <br><br>
        <div class="col-lg-18">
          <div class="accordions is-first-expanded">
          <button type="button" class="btn btn-outline-primary" data-toggle="modal" data-target="#RegisterManga">Cadastrar Manga</button>
          <br><br>
          <table id="table" name="table" class="table table-bordered table-hover" width="100%">
                <thead>
                    <tr>
                        <th>id</th>
                        <th>name</th>
                        <th>capitulos</th>
                        <th>status</th>
                        <th>data_lancamento</th>
                        <th>opcoes</th>
                    </tr>
                </thead>
                <tbody>
                </tbody>
            </table>
        </div>
      </div>
    </div>
  </section>


@include('layouts.mangamodal')
<script src="{{ asset('/js/datatable.js') }}"></script>

@endsection