PGDMP     *                     {            School    15.1    15.1 $               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16401    School    DATABASE        CREATE DATABASE "School" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Ukrainian_Ukraine.1251';
    DROP DATABASE "School";
                postgres    false            ?            1259    16456    schedule    TABLE     ?   CREATE TABLE public.schedule (
    schedule_id integer NOT NULL,
    subjects_id integer NOT NULL,
    teachers_id integer NOT NULL,
    students_id integer NOT NULL,
    week_day character varying(50) NOT NULL
);
    DROP TABLE public.schedule;
       public         heap    postgres    false            ?            1259    16455    Schedule_schedule_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."Schedule_schedule_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public."Schedule_schedule_id_seq";
       public          postgres    false    221                        0    0    Schedule_schedule_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public."Schedule_schedule_id_seq" OWNED BY public.schedule.schedule_id;
          public          postgres    false    220            ?            1259    16449    students    TABLE     ?   CREATE TABLE public.students (
    students_id integer NOT NULL,
    name character varying(50) NOT NULL,
    home_address character varying(50) NOT NULL,
    phone_number character varying(50) NOT NULL,
    email character varying(50) NOT NULL
);
    DROP TABLE public.students;
       public         heap    postgres    false            ?            1259    16448    Students_students_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."Students_students_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public."Students_students_id_seq";
       public          postgres    false    219            !           0    0    Students_students_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public."Students_students_id_seq" OWNED BY public.students.students_id;
          public          postgres    false    218            ?            1259    16435    subjects    TABLE     l   CREATE TABLE public.subjects (
    subjects_id integer NOT NULL,
    name character varying(50) NOT NULL
);
    DROP TABLE public.subjects;
       public         heap    postgres    false            ?            1259    16434    Subjects_subjects_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."Subjects_subjects_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public."Subjects_subjects_id_seq";
       public          postgres    false    215            "           0    0    Subjects_subjects_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public."Subjects_subjects_id_seq" OWNED BY public.subjects.subjects_id;
          public          postgres    false    214            ?            1259    16442    teachers    TABLE     ?   CREATE TABLE public.teachers (
    teachers_id integer NOT NULL,
    name character varying(50) NOT NULL,
    home_address character varying(50) NOT NULL,
    phone_number character varying(50) NOT NULL,
    email character varying(50) NOT NULL
);
    DROP TABLE public.teachers;
       public         heap    postgres    false            ?            1259    16441    Teachers_teachers_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."Teachers_teachers_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public."Teachers_teachers_id_seq";
       public          postgres    false    217            #           0    0    Teachers_teachers_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public."Teachers_teachers_id_seq" OWNED BY public.teachers.teachers_id;
          public          postgres    false    216            w           2604    16459    schedule schedule_id    DEFAULT     ~   ALTER TABLE ONLY public.schedule ALTER COLUMN schedule_id SET DEFAULT nextval('public."Schedule_schedule_id_seq"'::regclass);
 C   ALTER TABLE public.schedule ALTER COLUMN schedule_id DROP DEFAULT;
       public          postgres    false    220    221    221            v           2604    16452    students students_id    DEFAULT     ~   ALTER TABLE ONLY public.students ALTER COLUMN students_id SET DEFAULT nextval('public."Students_students_id_seq"'::regclass);
 C   ALTER TABLE public.students ALTER COLUMN students_id DROP DEFAULT;
       public          postgres    false    218    219    219            t           2604    16438    subjects subjects_id    DEFAULT     ~   ALTER TABLE ONLY public.subjects ALTER COLUMN subjects_id SET DEFAULT nextval('public."Subjects_subjects_id_seq"'::regclass);
 C   ALTER TABLE public.subjects ALTER COLUMN subjects_id DROP DEFAULT;
       public          postgres    false    215    214    215            u           2604    16445    teachers teachers_id    DEFAULT     ~   ALTER TABLE ONLY public.teachers ALTER COLUMN teachers_id SET DEFAULT nextval('public."Teachers_teachers_id_seq"'::regclass);
 C   ALTER TABLE public.teachers ALTER COLUMN teachers_id DROP DEFAULT;
       public          postgres    false    216    217    217                      0    16456    schedule 
   TABLE DATA           `   COPY public.schedule (schedule_id, subjects_id, teachers_id, students_id, week_day) FROM stdin;
    public          postgres    false    221   ?)                 0    16449    students 
   TABLE DATA           X   COPY public.students (students_id, name, home_address, phone_number, email) FROM stdin;
    public          postgres    false    219   ?*                 0    16435    subjects 
   TABLE DATA           5   COPY public.subjects (subjects_id, name) FROM stdin;
    public          postgres    false    215   ?+                 0    16442    teachers 
   TABLE DATA           X   COPY public.teachers (teachers_id, name, home_address, phone_number, email) FROM stdin;
    public          postgres    false    217   8,       $           0    0    Schedule_schedule_id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public."Schedule_schedule_id_seq"', 100655, true);
          public          postgres    false    220            %           0    0    Students_students_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."Students_students_id_seq"', 440, true);
          public          postgres    false    218            &           0    0    Subjects_subjects_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."Subjects_subjects_id_seq"', 433, true);
          public          postgres    false    214            '           0    0    Teachers_teachers_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."Teachers_teachers_id_seq"', 339, true);
          public          postgres    false    216            ?           2606    16461    schedule schedule_idPK 
   CONSTRAINT     _   ALTER TABLE ONLY public.schedule
    ADD CONSTRAINT "schedule_idPK" PRIMARY KEY (schedule_id);
 B   ALTER TABLE ONLY public.schedule DROP CONSTRAINT "schedule_idPK";
       public            postgres    false    221            }           2606    16454    students students_idPK 
   CONSTRAINT     _   ALTER TABLE ONLY public.students
    ADD CONSTRAINT "students_idPK" PRIMARY KEY (students_id);
 B   ALTER TABLE ONLY public.students DROP CONSTRAINT "students_idPK";
       public            postgres    false    219            y           2606    16440    subjects subjects_idPK 
   CONSTRAINT     _   ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT "subjects_idPK" PRIMARY KEY (subjects_id);
 B   ALTER TABLE ONLY public.subjects DROP CONSTRAINT "subjects_idPK";
       public            postgres    false    215            {           2606    16447    teachers teachers_idPK 
   CONSTRAINT     _   ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT "teachers_idPK" PRIMARY KEY (teachers_id);
 B   ALTER TABLE ONLY public.teachers DROP CONSTRAINT "teachers_idPK";
       public            postgres    false    217            ~           1259    16467    fki_subject_idFK    INDEX     N   CREATE INDEX "fki_subject_idFK" ON public.schedule USING btree (subjects_id);
 &   DROP INDEX public."fki_subject_idFK";
       public            postgres    false    221            ?           2606    16483    schedule students_idFK    FK CONSTRAINT     ?   ALTER TABLE ONLY public.schedule
    ADD CONSTRAINT "students_idFK" FOREIGN KEY (students_id) REFERENCES public.students(students_id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.schedule DROP CONSTRAINT "students_idFK";
       public          postgres    false    3197    219    221            ?           2606    16473    schedule subjects_idFK    FK CONSTRAINT     ?   ALTER TABLE ONLY public.schedule
    ADD CONSTRAINT "subjects_idFK" FOREIGN KEY (subjects_id) REFERENCES public.subjects(subjects_id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.schedule DROP CONSTRAINT "subjects_idFK";
       public          postgres    false    221    215    3193            ?           2606    16478    schedule teachers_idFK    FK CONSTRAINT     ?   ALTER TABLE ONLY public.schedule
    ADD CONSTRAINT "teachers_idFK" FOREIGN KEY (teachers_id) REFERENCES public.teachers(teachers_id) MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.schedule DROP CONSTRAINT "teachers_idFK";
       public          postgres    false    217    3195    221               ?   x?U???0Eg?cP?$M:A?/?Z??f?Gj????ח'I?2?"!4?)????a+?	?_Ǣ????"Lh??q???c{?r?~?t\??&???????cG?????xK?Z?f?ǽ?;???_C1??s??????qq?:?Wʠ?{?ƝH_?(۲?ؿ??|#?R?~>?鉛?c?????*?ˡi{?M????˕?Q*?ɡ-??c_h?Y?            x??Ir? ?s?1??X??(?"?E????9v*?z??C????h????i??!}( w?6?U	??? ???:?$???Xd?($:??D?h?nh???#\??j????|????qE;?~??5A???rаvx?gO?V3v9?e7?3?z7???v??ʚ?u?qC?PmI?ExcZ?
b;O?'H???Ā å?????!?????mG?t?????z?V?????o?N7??<?H?l?>?}M???-T?         -   x?316?tr??216??r2?8]Àc??[W? ??         =   x?366??tq??u??p??????26???w?t	w??t???r??????? I?     