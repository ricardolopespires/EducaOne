import Image from "next/image";
import Link from "next/link";

const Hero = () => {
  return (
    <div className="relative min-h-screen bg-gradient-to-br from-gray-50 to-blue-50/30">
      {/* Background Elements */}
      <div className="absolute inset-0">
        <div className="absolute top-0 right-0 w-6/12 h-full bg-gradient-to-l from-blue-50 to-transparent" />
        <div className="absolute bottom-0 left-0 w-full h-1/2 bg-gradient-to-t from-white to-transparent" />
      </div>
      
      <div className="container mx-auto px-4 pt-32 pb-20 relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          {/* Text Content */}
          <div className="pt-32">
            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 leading-tight">
              Gestão Condominial{" "}
              <span className="bg-gradient-to-r from-blue-600 to-teal-500 bg-clip-text text-transparent">
                Potencializada por IA
              </span>
            </h1>
            
            <p className="mt-6 text-lg text-gray-600 leading-relaxed">
              Revolucione a administração do seu condomínio com nossa plataforma que combina 
              inteligência artificial, análise de dados e automação para uma gestão mais eficiente 
              e moderna.
            </p>

            <div className="mt-8 flex flex-wrap gap-4">
              <Link 
                href="/demonstracao"
                className="px-8 py-4 bg-gradient-to-r from-blue-600 to-teal-500 text-white rounded-xl font-medium hover:opacity-90 transition-opacity shadow-lg shadow-blue-500/20"
              >
                Agendar Demonstração
              </Link>
              <Link 
                href="#recursos"
                className="px-8 py-4 bg-white text-gray-700 rounded-xl font-medium border border-gray-200 hover:border-blue-500 hover:text-blue-500 transition-colors shadow-lg shadow-gray-200/20"
              >
                Conhecer Recursos
              </Link>
            </div>

            {/* Trusted By Section */}
            <div className="mt-16">
              <p className="text-sm text-gray-500 mb-4">Utilizado pelos melhores condomínios</p>
              <div className="flex gap-8 items-center">
                <Image src="/images/alphaville.png" alt="Alphaville" width={100} height={40} className="opacity-60 hover:opacity-100 transition-opacity" />
                <Image src="/images/brookfield.png" alt="Brookfield" width={100} height={40} className="opacity-60 hover:opacity-100 transition-opacity" />
                <Image src="/images/cyrela.png" alt="Cyrela" width={100} height={40} className="opacity-60 hover:opacity-100 transition-opacity" />
              </div>
            </div>

            {/* User Stats */}
            <div className="mt-16 flex items-center gap-6 bg-white/80 backdrop-blur-sm p-4 rounded-2xl w-fit">
              <div className="flex -space-x-3">
                {[1, 2, 3].map((i) => (
                  <div key={i} className="w-12 h-12 rounded-full border-2 border-white overflow-hidden shadow-lg">
                    <Image
                      src={`/images/avatars/admin${i}.jpg`}
                      alt={`Administrador ${i}`}
                      width={48}
                      height={48}
                      className="w-full h-full object-cover"
                    />
                  </div>
                ))}
              </div>
              <div>
                <p className="font-semibold text-gray-900">+1.500 Condomínios</p>
                <div className="flex items-center gap-1">
                  {[1, 2, 3, 4, 5].map((star) => (
                    <svg key={star} className="w-4 h-4 text-yellow-400" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                    </svg>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Image Section */}
          <div className="relative lg:h-[600px]">
            <div className="relative h-full w-full">
              <Image
                src="/images/dashboard-preview.png"
                alt="Dashboard Inteligente"
                fill
                className="object-contain"
                priority
              />
              
              {/* Floating Stats Card */}
              <div className="absolute top-1/4 -left-10 bg-white rounded-2xl p-4 shadow-lg max-w-xs">
                <div className="flex items-center gap-5">
                  <div className="w-8 h-8 rounded-full bg-blue-700 flex items-center justify-center text-white text-sm font-bold">
                    <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                    </svg>
                  </div>
                  <div>
                    <p className="text-sm font-medium">Economia Mensal</p>
                    <p className="text-xs text-gray-500">R$ 15.5k</p>
                  </div>
                </div>
              </div>
                 {/* Analytics Card */}
                 <div className="absolute bottom-4 right-4 bg-white rounded-2xl p-4 shadow-lg max-w-xs">
                <div className="flex items-start gap-3">
                  <div className="w-8 h-8 rounded-full bg-blue-700 flex items-center justify-center text-white text-sm font-bold">
                    AI
                  </div>
                  <div>
                    <p className="text-sm font-medium">Análise Preditiva</p>
                    <p className="text-xs text-gray-500">Economia prevista: 22%</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Hero;
  