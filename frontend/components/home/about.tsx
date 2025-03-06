import Image from 'next/image';
import { FaPlay } from 'react-icons/fa';

const About = () => {
  return (
    <section className="py-20 bg-white">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
        {/* Coluna da Imagem com Vídeo */}
        <div className="relative">
          <div className="relative h-[600px] rounded-lg overflow-hidden">
            <Image
              src="/images/about-interior.jpg"
              alt="Interior Moderno"
              fill
              className="object-cover"
            />
            <div className="absolute inset-0 bg-black/20"></div>
            <button className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white rounded-full p-5 hover:bg-blue-600 transition-colors group">
              <FaPlay className="w-6 h-6 text-blue-600 group-hover:text-white" />
            </button>
          </div>
        </div>

        {/* Coluna do Conteúdo */}
        <div className="px-6 lg:px-12">
          <h3 className="text-blue-600 font-medium mb-4">BEM-VINDO AO SMARTCITY</h3>
          <h2 className="text-4xl font-bold mb-6">
            INOVAÇÃO INTELIGENTE
            <br />
            GESTÃO MODERNA
          </h2>
          <p className="text-gray-600 mb-8">
            Com mais de 25 anos de experiência, o SmartCity revoluciona a forma como os condomínios são gerenciados. 
            Nossa plataforma combina tecnologia de ponta com simplicidade de uso, garantindo uma gestão eficiente e moderna 
            para seu condomínio.
          </p>

          <div className="grid grid-cols-2 gap-8 mb-8">
            <div>
              <h4 className="text-3xl font-bold text-blue-600 mb-2">25+</h4>
              <p className="text-gray-600">Anos de Experiência</p>
            </div>
            <div>
              <h4 className="text-3xl font-bold text-blue-600 mb-2">1.250+</h4>
              <p className="text-gray-600">Projetos Concluídos</p>
            </div>
          </div>

          <button className="bg-blue-600 text-white px-8 py-3 rounded hover:bg-blue-700 transition-colors">
            SAIBA MAIS
          </button>
        </div>
      </div>
    </section>
  );
};

export default About; 