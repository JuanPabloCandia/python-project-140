# filepath: c:\Users\Digital Optimizer\Desktop\python-project-140-main\spec\10_brain_games_spec.rb
require 'spec_helper'

RSpec.describe 'bin/brain-games', type: :aruba do
  let(:file_path) do
    base_dir = File.expand_path('../.venv', __dir__)
    executable_dir = File::ALT_SEPARATOR ? 'Scripts' : 'bin' # Detecta Windows o Unix/Linux
    File.join(base_dir, executable_dir, 'brain-games')
  end

  before(:each) do
    unless File.exist?(file_path)
      raise "El archivo ejecutable no se encuentra en la ruta esperada: #{file_path}"
    end
    run_command file_path
  end

  before(:each) do
    expect(last_command_started).not_to be_stopped
    type('Tirion')
  end

  it 'works' do
    expect(last_command_started).to be_stopped
    expect(last_command_started).to be_successfully_executed
    expect(last_command_started).to have_output /Welcome to the Brain Games!/
    expect(last_command_started).to have_output /May I have your name?/
    expect(last_command_started).to have_output /Hello, Tirion/
  end
end