CREATE TABLE professores(
    id int not null primary key autoincrement,
    nome text,
    email text,
    telefone text
);

CREATE TABLE disciplinas(
    id int not null primary key autoincrement,
    nome text,
    carga_horaria int
);

CREATE TABLE turmas(
    id int not null primary key autoincrement,
    nome text,
    ano_letivo int,
    turno text
);

CREATE TABLE alunos(
    id int not null primary key autoincrement,
    nome text,
    data_nascimento text,
    email text,
    turma_id int,
    foreign key (turma_id) references turmas(id)
);

CREATE TABLE aulas(
    id int not null primary key autoincrement,
    dia_semana int,
    inicio text,
    fim text,
    sala text,
    turma_id int,
    foreign key (turma_id) references turmas(id),
    disciplina_id int,
    foreign key (disciplina_id) references disciplinas(id),
    professore_id int,
    foreign key (professore_id) references professores(id)
);